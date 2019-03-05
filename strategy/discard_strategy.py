import random
from typing import List, Callable
from models.photo import Photo
from config import Config


def keep_all(photos: List[Photo]) -> List[Photo]:
    """Keep the initial set."""

    return photos


def discard_outlier(photos: List[Photo]) -> List[Photo]:
    """Discard photos whose number of tags diverge from set mean by margin."""

    assert 0 <= Config.DISCARD_PERCENT < 1

    if Config.DISCARD_PERCENT == 0:
        return photos

    number_tags = [len(p.tags) for p in photos]
    avg = sum(number_tags)/(len(number_tags))
    l_bound = avg - (avg * Config.DISCARD_PERCENT)
    u_bound = avg + (avg * Config.DISCARD_PERCENT)

    aux = [p for p in photos if l_bound <= len(p.tags) <= u_bound]
    if len([p for p in aux if p.orientation == 'V']) % 2 == 1:
         # Even vertical photos constriction not respected
         unused_vertical = [p for p in photos if p.orientation == 'V' and \
                                              p not in aux]
         aux.append(unused_vertical[0])

    photos = aux
    return photos


def discard_random(photos: List[Photo]) -> List[Photo]:
    """Discard a random percent of the photos from the set."""

    assert 0 <= Config.DISCARD_PERCENT < 1

    percent_keep = 1 - Config.DISCARD_PERCENT
    horizontal = [p for p in photos if p.orientation == 'H']
    vertical = [p for p in photos if p.orientation == 'V']
    h_keep = int(len(horizontal) * percent_keep)
    v_keep = int(len(vertical) * percent_keep)
    if v_keep % 2 == 1:
        v_keep += 1

    horizontal = random.sample(horizontal, h_keep)
    vertical = random.sample(vertical, v_keep)

    return horizontal + vertical
