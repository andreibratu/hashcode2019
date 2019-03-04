from typing import List
from models.photo import Photo


class Slide:

    def __init__(self, photo1: Photo, photo2: Photo = None):
        if photo2 is not None:
            assert photo1.orientation == 'V' and photo2.orientation == 'V'
        self.photo1 = photo1
        self.photo2 = photo2

    def __str__(self):
        if self.photo2 is None:
            return f'SLIDE: {self.photo1} None\n'
        else:
            return f'SLIDE: {self.photo1} {self.photo2}\n'

    def get_tags(self) -> List[str]:
        if self.photo2 is None:
            return self.photo1.tags
        else:
            return self.photo1.tags + self.photo2.tags

    __repr__ = __str__


def calculate_interesting_factor(slide1: Slide, slide2: Slide) -> int:
    """Calculate interesting factor between two given slides."""

    photo1_tags = set(slide1.get_tags())
    photo2_tags = set(slide2.get_tags())

    # Set operations return a new set
    only_photo1 = len(photo1_tags-photo2_tags)
    only_photo2 = len(photo2_tags-photo1_tags)
    in_both_photos = len(photo1_tags&photo2_tags)

    return min(min(only_photo1, only_photo2), in_both_photos)
