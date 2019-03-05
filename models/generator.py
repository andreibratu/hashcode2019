import random
from queue import Queue
from threading import Thread
from typing import List, Callable
from models.photo import Photo
from models.slide import Slide
from models.individual import Individual


class Generator:
    """Generate Individual objects from an input of Photo objects."""

    id = 0

    def __init__(self, photos: List[Photo], discard_strategy: Callable):
        photos = discard_strategy(photos)
        self.discard_strategy = discard_strategy
        self.v_photos = [p for p in photos if p.orientation == 'V']
        self.h_photos = [p for p in photos if p.orientation == 'H']
        self.id = Generator.id
        Generator.id += 1


    def attach_meta(self, individuals: List[Individual]) -> List[Individual]:
        for i in individuals:
            assert hasattr(i, 'meta')
            i.meta.update({
                'discard': self.discard_strategy.__name__
            })
            assert 'discard' in i.meta

        return individuals


    def generate(self, how_many: int) -> List[Individual]:
        def generate_individual(q, result):
            while not q.empty():
                idx = q.get()

                print(f'GENERATOR {self.id} INDIVIDUAL {idx}')

                slides = []
                slides += [Slide(p, None) for p in self.h_photos]
                v_used_ids = set()

                while len(v_used_ids) != len(self.v_photos):
                    # While not all vertical photos were used
                    unused_vertical_ids = vertical_photo_ids-v_used_ids
                    idx1_v, idx2_v = random.sample(unused_vertical_ids, 2)
                    for p in self.v_photos:
                        if p.id == idx1_v:
                            photo1_v = p
                        if p.id == idx2_v:
                            photo2_v = p
                    slides.append(Slide(photo1_v, photo2_v))
                    v_used_ids.add(idx1_v)
                    v_used_ids.add(idx2_v)

                random.shuffle(slides)
                result[idx] = Individual(slides)

                q.task_done()
            return True

        result = [None for _ in range(how_many)]
        vertical_photo_ids = set([p.id for p in self.v_photos])
        work_q = Queue(maxsize=0)
        num_threads = min(50, how_many)

        for i in range(how_many):
            work_q.put(i)

        for i in range(num_threads):
            worker = Thread(target=generate_individual, args=[work_q, result])
            worker.start()

        work_q.join()
        return self.attach_meta(result)
