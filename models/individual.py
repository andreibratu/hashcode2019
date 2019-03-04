from typing import List
from models.slide import Slide, calculate_interesting_factor


class Individual:

    def __init__(self, slides: List[Slide]):
        self.slides = slides
        self.vertical_slides = [s for s in slides if s.photo2 is not None]
        self.calculate_fitness()

    def calculate_fitness(self):
        fitness = 0
        slideshow_length = len(self.slides)
        for i in range(slideshow_length-1):
            fitness += calculate_interesting_factor(
                self.slides[i],
                self.slides[i+1]
            )
        self.fitness = fitness


    def __str__(self):
        return f'INDIVIDUAL {self.fitness}'


    __repr__ = __str__
