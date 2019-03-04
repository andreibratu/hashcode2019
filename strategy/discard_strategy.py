import random
from typing import List, Callable
from models.photo import Photo


def keep_all_photos(photos: List[Photo]):
    """Keep the initial set."""

    pass


def discard_outliers(margin: float) -> Callable:
    """Discard photos whose number of tags diverge from set mean by margin."""

    def f(photos: List[Photo]) -> List[Photo]:
        number_tags = [len(p.tags) for p in photos]
        avg = sum(number_tags)/(len(number_tags))
        l_bound = avg - (avg * float)
        u_bound = avg + (avg * float)

        return [p for p in photos if l_bound <= len(p.tags) <= u_bound]

    assert 0 < margin < 1
    return f


def discard_random(percent: float) -> Callable:
    """Discard a random percent of the photos from the set."""

    def f(photos: List[Photo]) -> List[Photo]:
        how_many_remain = len(photo) - int(len(photo) * percent)
        return random.sample(photos, how_many_remain)

    assert 0 < margin < 1
    return f
