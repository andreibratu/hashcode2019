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
