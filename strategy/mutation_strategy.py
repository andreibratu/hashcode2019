import random
from numpy.random import choice
from typing import Callable
from models.individual import Individual
from models.slide import Slide


def swap_photos_slide(i: Individual) -> Individual:
    """Find a vertical slide in individual and swap its photos."""

    aux = i.slides[:]
    v_slides = [s for s in aux if s.photo2 is not None]
    if len(v_slides) == 0:
        return i

    mutate_slide = random.sample(v_slides, 1)[0]
    idx = aux.index(mutate_slide)

    p = Slide(aux[idx].photo2, aux[idx].photo1)
    aux[idx] = p
    i.slides = aux
    return i


def swap_slides(i: Individual) -> Individual:
    """Swap two slides from individual."""

    aux = i.slides[:]
    idx1, idx2 = random.sample(range(0, len(aux)), 2)
    aux[idx1], aux[idx2] = aux[idx2], aux[idx1]
    assert aux != i.slides
    i.slides = aux
    return i


def random_mutation(i: Individual) -> Individual:
    """Apply random mutation on the individual."""

    f = choice([swap_photos_slide, swap_slides])
    return f(i)
