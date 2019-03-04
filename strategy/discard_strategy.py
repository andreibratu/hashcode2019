import random
from typing import List, Callable

from models.photo import Photo

from config import Config


def _add_vertical_photo(old_set: List[Photo], new_set: List[Photo]):
    """Auxiliary function that mentains the even vertical photos restriction.

    Function appends to `new_set` a vertical photo that is not in it.
    """

    vertical_photos_remain = [p for p in new_set if p.orientation == 'V']
    # Check if vertical photos are in even number
    if len(vertical_photos_remain) % 2 == 0:
        # Odd number of vertical photos, add one more
        vertical_photo = [p for p in old_set \
                          if p.orientation == 'V' and p not in new_set][0]
        old_set.append(vertical_photo)


def keep_all(photos: List[Photo]) -> List[Photo]:
    """Keep the initial set."""

    return photos


def discard_outlier(photos: List[Photo]) -> List[Photo]:
    """Discard photos whose number of tags diverge from set mean by margin."""

    assert 0 < Config.DISCARD_PER < 1

    number_tags = [len(p.tags) for p in photos]
    avg = sum(number_tags)/(len(number_tags))
    l_bound = avg - (avg * Config.DISCARD_PER)
    u_bound = avg + (avg * Config.DISCARD_PER)

    remain = [p for p in photos if l_bound <= len(p.tags) <= u_bound]

    assert len(remain) != 0
    _add_vertical_photo(photos, remain)

    assert remain is not None

    return remain


def discard_random(photos: List[Photo]) -> List[Photo]:
    """Discard a random percent of the photos from the set."""

    assert 0 < Config.DISCARD_PER < 1

    how_many_remain = len(photo) - int(len(photo) * Config.DISCARD_PER)

    remain = random.sample(photos, how_many_remain)
    assert len(remain) != 0
    _add_vertical_photo(photos, remain)
    assert len(remain) != 0

    return remain
