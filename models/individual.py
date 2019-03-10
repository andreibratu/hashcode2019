from typing import List
from models.slide import Slide
from interesting import calculate_interesting_factor

class Individual:

    id = 0

    def __init__(self, slides):
        self.slides = slides
        self.fitness = 0
        self.id = Individual.id

        Individual.id += 1


    def calculate_fitness(self):
        fitness = 0
        slideshow_length = len(self.slides)
        for i in range(slideshow_length-1):
            fitness += calculate_interesting_factor(
                self.slides[i],
                self.slides[i+1]
            )
        self.fitness = fitness


    def add_slide(self, s: Slide):
        self.slides.append(s)
        if s.photo2 is not None:
            self.vertical_slides.append(s)
            assert s.photo2.id not in self.photo_ids
            self.photo_ids.add(s.photo2.id)
        assert s.photo1.id not in self.photo_ids
        self.photo_ids.add(s.photo1.id)


    def validate(self):
        ids = set()
        for s in self.slides:
            if s.photo2 is not None:
                if s.photo2.id in ids:
                    raise ValueError
                ids.add(s.photo2.id)
            if s.photo1.id in ids:
                raise ValueError
            ids.add(s.photo1.id)


    def __str__(self):
        return f'INDIVIDUAL {self.id}'
