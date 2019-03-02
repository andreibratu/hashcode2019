import random

from photo import Photo
from slide import Slide
from individual import Individual
from util import read_input, write_output
from generate import generate_individual, generate_photo_series

from strategies import tuple_cross, no_mutation_strategy, swap_photos_strategy,
                       everybody_lives


############# HYPERPARAMS #############
GENERATIONS = 1000
OFFSPRINGS = 100
DIE_INDIVIDUALS = 0
MUTATATION_PROB = 0.1

############# AUX #############
def select_individual(pool, total_fitnesss):
    """Select individuals with a bias towards fit ones."""
    aim = random.randrange(0, total_fitness)
    seen_fitness = 0
    for i in pool:
        if seen_fitness >= aim:
            return i
        else:
            seen_fitness += i.fitness


############# MAIN LOOP #############
photos = read_input("a_example.txt")


individuals = []

for _ in range(SLIDES_FROM_SERIE):
    individual = generate_individual(photos)
    slides = []
    for idx1, idx2 in individual:
        p1 = photos[idx1]
        p2 = None
        if idx2 is not None:
            p2 = photos[idx2]
        s = Slide(p1, p2)
        slides.append(s)

    individuals.append(Individual(slides))


pool = Pool(
    population = individuals,
    cross_strategy = tuple_cross(3),
    mutation_strategy = no_mutation_strategy,
    extinction_strategy = everybody_lives,
    new_indiviuals_setting = OFFSPRINGS,
    die_individuals_setting = DIE_INDIVIDUALS,
    mutation_probability = MUTATATION_PROB
)

for _ in range(GENERATIONS):
    pool.evolve()

write_output(pool.get_best_individual(), "output.txt")
