import random
from queue import Queue
from threading import Thread
from typing import List, Callable
from models.photo import Photo
from models.slide import Slide
from models.individual import Individual
from config import DISCARD_PERCENT


class Generator:
    """Generate Individual objects from an input of Photo objects."""

    def __init__(self, photos: List[Photo], discard_strategy: Callable):
        photos = discard_strategy(photos)
        self.v_photos = [p for p in photos if p.orientation == 'V']
        self.h_photos = [p for p in photos if p.orientation == 'H']


    def generate(self, how_many: int) -> List[Individual]:
        def generate_individual(q, result):
            while not q.empty():
                idx = q.get()

                print(f'GENERATOR {self.idx} INDIVIDUAL {idx}')

                slides = []
                slides += [Slide(p, None) for p in self.h_photos]
                v_used_ids = set()

                while len(v_used_ids) != len(self.v_photos):
                    unused_vertical_ids = vertical_photo_ids-v_used_ids
                    idx1_v, idx2_v = random.sample(unused_vertical_ids, 2)
                    photo1_v = self.v_photos[idx1_v]
                    photo2_v = self.v_photos[idx2_v]
                    slides.append(Slide(photo1_v, photo2_v))

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

        return result
