import random
from typing import Callable, List
from individual import Individual
from photo import Photo


def tuple_cross(tuple_size: int) -> Callable:
    """Cross two individuals."""

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
