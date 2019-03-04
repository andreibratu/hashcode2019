from typing import Callable
from models.individual import Individual


def no_mutation(i: Individual) -> Individual:
    """Individuals do not suffer random mutations."""

    return i


def swap_photos_in_slide(i: Individual) -> Individual:
    """Find a vertical slide in individual and swap its photos."""

    if len(i.vertical_slides) == 0:
        return i

    mutate_slide = random.sample(i.vertical_slides, 1)[0]

    mutate_slide.photo1, mutate_slide[idx].photo2 = \
        mutate_slide[idx].photo2, mutate_slide.photo1
    # Mutation done by reference, assertion should be fine
    assert mutate_slide in i.slides
    return i
