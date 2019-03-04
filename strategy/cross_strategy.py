import random
from typing import Callable, List
from models.individual import Individual
from models.photo import Photo


def slice_cross(tuple_size: int) -> Callable:
    """Cross two individuals by alternating slices.

    The strategy assumes that over time, individuals will start to display
    subsequences with a good interesting factor, that would be lost if
    we alternated by a slide. A problem that might arise with this strategy
    is that for a big `tuple_size` arguement, the algorithm might be
    stuck with long random subsequences, leading to a slow evolution.
    """

    def f(i1: Individual, i2: Individual) -> Individual:
        flag_select_first = True
        new_slides = []
        last_index = 0

        for idx in range(0, len(i1.slides), tuple_size):
            if flag_select_first:
                new_slides += i1.slides[idx:idx+tuple_size+1]
            else:
                new_slides += i2.slides[idx:idx+tuple_size+1]
            flag_select_first = not flag_select_first
            last_index = idx

        if len(new_slides) < len(i1.slides):
            if flag_select_first:
                new_slides += i1.slides[last_index:]
            else:
                new_slides += i2.slides[last_index:]

        return Individual(new_slides)

    return f


def adaptive_slice_cross(total_generations: int, step: int) -> Callable:
    """Cross two individuals by alternating larger and larger slices.

    This strategy builds upon the assumption of better slices over time made
    in `slice_cross` by combining larger and larger slices. The size used
    by the adaptive algorithm is determined by splitting the `GENERATIONS`
    param into `step` intervals. A generation in interval `t` is assigned
    a step `t` for the tuple cross.
    """

    interval_size = total_generations // step
    left_end_interval = 0
    right_end_interval = interval_size - 1
    interval = 1
    while True:
        if left_end_interval <= step <= right_end_interval:
            break
        else:
            left_end_interval = right_end_interval
            right_end_interval += interval_size
            interval += 1
    return slice_cross(interval)
