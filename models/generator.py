import random
from typing import List, Callable
from models.photo import Photo
from models.slide import Slide
from sklearn.preprocessing import OneHotEncoder


class Generator:
    """Generate random slideshow from given photos."""

    def __init__(self, photos: List[Photo]):
        self.slides = []
        self.photos = photos
        self.generate_slides()


    def generate_slides(self) -> List[Slide]:
        print('Generating slides..')
        h_slides = [Slide(p, None) for p in self.photos if p.orientation == 'H']
        v_slides = []
        v_photos = [p for p in self.photos if p.orientation == 'V']

        while v_photos != []:
            p1, p2 = random.sample(v_photos, 2)
            v_photos.remove(p1)
            v_photos.remove(p2)
            v_slides.append(Slide(p1, p2))

        self.slides = h_slides + v_slides


    def get_slideshow(self) -> List[Slide]:
        random.shuffle(self.slides)
        return self.slides
