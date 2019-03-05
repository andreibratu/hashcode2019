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

discard_strategies = [keep_all, discard_outlier, discard_random]
extinction_strategies = [no_remove]
mutation_strategies = [no_mutation]
cross_strategies = [adaptive_slice_cross]

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
print('GENERATING INDIVIDUALS\n******')
for g in generators:
    g.idx = g_idx
    # Threaded generator might fail and return None individuals, discard them
    generated = set(g.generate(Config.INIT_INDIVIDUALS))
    empty_set = set([None])
    individuals_sets.append(list(generated-empty_set))
    g_idx += 1
    print('******')

print('\nSTARTING EVOLUTION PROCESS\n******')
for population in individuals_sets:
    for es in extinction_strategies:
        for ms in mutation_strategies:
            for cs in cross_strategies:
                Config.CURR_GENERATION = 0

                pool = Pool(
                    population=population,
                    extinction_strategy=es,
                    mutation_strategy=ms,
                    cross_strategy=cs,
                )

                for g in range(Config.GENERATIONS):
                    Config.CURR_GENERATION += 1
                    pool.evolve()
                    pool.set_best_individual()
                    bf = pool.population[-1].fitness
                    print(f'POOL {pool.id} GENERATION {g} FITNESS {bf}')

                pool.set_best_individual()
                best_individuals.append(pool.best)
                print(pool.best.meta)

best_individuals.sort(key=lambda i: i.fitness)
best = best_individuals[-1]
print(f'Top dog: {best.fitness} -- {best.meta}')
# write_output(best_individuals[-1], "output.txt")
