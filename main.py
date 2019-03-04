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

from config import Config
from util import read_input, write_output


random.seed(None)
photos = read_input("b_lovely_landscapes.txt")

# discard_strategies = [keep_all, discard_outlier, discard_random]
discard_strategies = [keep_all]
extinction_strategies = [no_remove, rm_least_fit, rm_random]
mutation_strategies = [no_mutation, swap_photos_in_slide]
cross_strategies = [slice_cross]

generators = []
individuals_sets = []
pools = []
best_individuals = []

for s in discard_strategies:
    g = Generator(
        photos=photos,
        discard_strategy=s,
    )
    generators.append(g)

g_idx = 0
print('GENERATING INDIVIDUALS\n******\n')
for g in generators:
    g.idx = g_idx
    # Threaded generator might fail and return None individuals, discard them
    generated = set(g.generate(Config.INIT_INDIVIDUALS))
    empty_set = set([None])
    individuals_sets.append(list(generated-empty_set))
    g_idx += 1
    print('******')

print('\nSTARTING EVOLUTION PROCESS\n')
p_idx = 0
for population in individuals_sets:
    for es in extinction_strategies:
        for ms in mutation_strategies:
            for cs in cross_strategies:
                Config.CURR_GENERATION = 0

                pool = Pool(
                    idx=p_idx,
                    population=population,
                    extinction_strategy=es,
                    mutation_strategy=ms,
                    cross_strategy=cs,
                )

                for g in range(Config.GENERATIONS):
                    Config.CURR_GENERATION += 1
                    pool.evolve()
                    bf = pool.population[-1].fitness
                    print(f'POOL {p_idx+1} GENERATION {g} FITNESS {bf}')

                pool.set_best_individual()
                best_individuals.append(pool.best)
                p_idx += 1

# write_output(pool.get_best_individual(), "output.txt")
