import random
from typing import List, Callable
from photo import Photo
from individual import Individual
from slide import Slide


class Generator:
    """Generate Individual objects from an input of Photo objects.

    The Generator applies heuristics on the input photo set.
    """

    def __init__(self, photos: List[Photo], discard_strategy: Callable,
                 discard_v_per: float, discard_h_per: float):
        self.v_photos = [p for p in photos if p.orientation == 'V']
        self.h_photos = [p for p in photos if p.orientation == 'H']
        self.discard_strategy = discard_strategy
        self.discard_v_per = discard_v_per
        self.discard_h_per = discard_h_per
        self.apply_discard_strategy()


    def apply_discard_strategy(self):
        if self.discard_v_per > 0:
            self.v_photos = self.discard_strategy(self.v_photos, discard_v_per)
        if self.discard_h_per > 0:
            self.h_photos = self.discard_strategy(self.h_photos, discard_h_per)


    def generate(self) -> Individual:
        aux_v = self.v_photos[:]
        aux_h = self.h_photos[:]
        assert len(aux_v) % 2 == 0

        slides = []
        slides += [Slide(p, None) for p in aux_h]

        while len(aux_v) != 0:
            # ValueError raised by randrange(0, 0) i.e.
            # list contains one element
            try:
                idx1_v = random.randrange(0, len(aux_v)-1)
            except ValueError:
                idx1_v = 0
            finally:
                photo1_v = aux_v[idx1_v]
                aux_v.pop(idx1_v)

            try:
                idx2_v = random.randrange(0, len(aux_v)-1)
            except ValueError:
                idx2_v = 0
            finally:
                photo2_v = aux_v[idx2_v]
                aux_v.pop(idx2_v)

            slides.append(Slide(photo1_v, photo2_v))

        random.shuffle(slides)
        return Individual(slides)
