import random
from typing import List, Callable
from models.photo import Photo


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

        remain = [p for p in photos if l_bound <= len(p.tags) <= u_bound]
        _add_vertical_photo(photos, remain)

        return remain

    assert 0 < margin < 1
    return f


def discard_random(percent: float) -> Callable:
    """Discard a random percent of the photos from the set."""

    def f(photos: List[Photo]) -> List[Photo]:
        how_many_remain = len(photo) - int(len(photo) * percent)

        remain = random.sample(photos, how_many_remain)
        _add_vertical_photo(photos, remain)

    assert 0 < margin < 1
    return f
