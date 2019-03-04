import random
from photo import Photo
from slide import Slide
from individual import Individual
from generator import Generator
from pool import Pool
from util import read_input, write_output
from cross_strategy import tuple_cross
from discard_strategy import keep_all_photos
from mutation_strategy import no_mutation, swap_photos_in_slide
from extinction_strategy import everybody_lives


############# HYPERPARAMS #############


INIT_INDIVIDUALS = 5
GENERATIONS = 1000
OFFSPRINGS = 20
DIE_INDIVIDUALS = 0
MUTATATION_PROB = 0.1


############# MAIN LOOP #############

random.seed(None)
photos = read_input("b_lovely_landscapes.txt")

generator = Generator(
    photos=photos,
    discard_strategy=keep_all_photos,
    discard_v_per=0,
    discard_h_per=0
)

# Threaded generator might fail and return None individuals, discard them
individuals = set(generator.generate(INIT_INDIVIDUALS)) - set([None])

pool = Pool(
    population = list(individuals),
    cross_strategy = tuple_cross(3),
    mutation_strategy = no_mutation,
    extinction_strategy = everybody_lives,
    new_individuals_setting = OFFSPRINGS,
    die_individuals_setting = DIE_INDIVIDUALS,
    mutation_probability = MUTATATION_PROB
)

for _ in range(GENERATIONS):
    pool.evolve()
    print(f'GENERATION {_} FITNESS: {pool.population[-1].fitness}')

write_output(pool.get_best_individual(), "output.txt")
