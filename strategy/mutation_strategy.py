import random
from typing import Callable
from models.individual import Individual


def no_mutation(i: Individual) -> Individual:
    """Individuals do not suffer random mutations."""

    return i


def swap_photos_slide(i: Individual) -> Individual:
    """Find a vertical slide in individual and swap its photos."""

    if len(i.vertical_slides) == 0:
        return i

    mutate_slide = random.sample(i.vertical_slides, 1)[0]

    mutate_slide.photo1, mutate_slide.photo2 = \
        mutate_slide.photo2, mutate_slide.photo1
    return i


def swap_slides(i: Individual) -> Individual:
    """Swap two slides from individual."""

    idx1, idx2 = random.sample(range(0, len(i.slides)), 2)
    i.slides[idx1], i.slides[idx2] = i.slides[idx2], i.slides[idx1]
    return i


def remove_random_slide(i: Individual) -> Individual:
    """Remove random slide from individual."""

    idx = random.sample(range(0, len(i.slides)), 1)[0]
    i.slides = i.slides[:idx] + i.slides[idx+1:]
    return i


def random_mutate(i: Individual) -> Individual:
    """Apply random mutation on the individual."""

    f = random.sample([swap_photos_slide, swap_slides, remove_random_slide], 1)
    return f[0](i)
