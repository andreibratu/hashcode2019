from slide import Slide, calculate_interesting_factor
from typing import List


class Individual:

    def __init__(self, slides: List[Slide]):
        self.slides = slides
        self.fitness = 0

    def calculate_fitness(self):
        fitness = 0
        slideshow_length = len(self.slides)
        for i in range(slideshow_length-1):
            fitness += calculate_interesting_factor(
                self.slides[i],
                self.slides[i+1]
            )
            self.fitness = fitness
