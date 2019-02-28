from util import calculate_interesting_factor


class Slide:

    def __init__(self, photo1, photo2 = None):
        if photo2 is not None:
            assert photo1.orientation == 'V' and photo2.orientation == 'V'
        self.photo1 = photo1
        self.photo2 = photo2

    def __str__(self):
        if photo2 is None:
            return str(self.photo1.id)
        else:
            return f'{photo1.id} {photo2.id}'


class Individual:

    def __init__(self, slides):
        self.slides = slides
        self.fitness = 0

    def calculate_fitness(self):
        fitness = 0
        slides_l = len(self.slides)
        for i in range(slides_l-1):
            fitness += calculate_interesting_factor(self.slides[i], self.slides[i+1])
        self.fitness = fitness
