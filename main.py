import random

from models.photo import Photo
from models.slide import Slide
from models.individual import Individual
from models.generator import Generator
from models.pool import Pool

from strategy.cross_strategy import slice_cross, adaptive_slice_cross
from strategy.discard_strategy import keep_all, discard_outlier, discard_random
from strategy.mutation_strategy import no_mutation, swap_photos_in_slide
from strategy.extinction_strategy import no_remove, rm_least_fit, rm_random

from config import (GENERATIONS, INIT_INDIVIDUALS, CURR_GENERATION)

from util import read_input, write_output


random.seed(None)
photos = read_input("b_lovely_landscapes.txt")

discard_strategies = [keep_all, discard_outlier, discard_random]
extinction_strategies = [no_remove, rm_least_fit, rm_random]
mutation_strategies = [no_mutation, swap_photos_in_slide]
cross_strategies = [slice_cross, adaptive_slice_cross]

generators = []
individuals_sets = []
pools = []
best_individuals = []

for s in discard_strategies:
    g = Generator(
        photos=photos,
        discard_strategy=keep_all,
    )
    generators.append(g)

g_idx = 0
for g in generators:
    g.idx = g_idx
    # Threaded generator might fail and return None individuals, discard them
    generated = set(g.generate(INIT_INDIVIDUALS))
    empty_set = set([None])
    individuals_sets.append(list(generated-empty_set))
    g_idx += 1
    print('******')

pool_idx = 0
for population in individuals_sets:
    for es in extinction_strategies:
        for ms in mutation_strategies:
            for cs in cross_strategies:
                CURR_GENERATION = 0

                pool = Pool(
                    population=population,
                    extinction_strategy=es,
                    mutation_strategy=ms,
                    cross_strategy=cs,
                )

                for g in range(GENERATIONS):
                    CURR_GENERATION += 1
                    pool.evolve()
                    bf = pool.population[-1].fitness
                    print(f'POOL {pool_idx} GENERATION {g} FITNESS {bf}')

                best_individuals.append(pool.get_best_individual())
                print('******')

write_output(pool.get_best_individual(), "output.txt")
