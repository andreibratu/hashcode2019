from typing import List
from models.photo import Photo


class Slide:

    id = 0

    def __init__(self, photo1: Photo, photo2: Photo = None):
        if photo2 is not None:
            assert photo1.orientation == 'V' and photo2.orientation == 'V'
        self.photo1 = photo1
        self.photo2 = photo2
        self.id = Slide.id

        Slide.id += 1


    def get_tags(self) -> List[str]:
        if self.photo2 is None:
            return self.photo1.tags
        else:
            return self.photo1.tags + self.photo2.tags
