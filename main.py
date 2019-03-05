import random
import itertools

from models.photo import Photo
from models.slide import Slide
from models.individual import Individual
from models.generator import Generator
from models.pool import Pool

from strategy.cross_strategy import slice_cross, adaptive_slice_cross
from strategy.discard_strategy import keep_all, discard_outlier, discard_random
from strategy.mutation_strategy import no_mutation, swap_photos_slide, \
                                       remove_random_slide, swap_slides, \
                                       random_mutation_strategy
from strategy.extinction_strategy import no_remove, rm_least_fit, rm_random

from config import Config
from util import read_input, write_output


random.seed(None)
photos = read_input("b_lovely_landscapes.txt")

disc_strat = [keep_all]
ext_strat = [no_remove]
mut_strat = [no_mutation]
cross_strat = [slice_cross]

######
generators = []
populations = []
pools = []
best_individuals = []
######

for s in disc_strat:
    g = Generator(
        photos=photos,
        discard_strategy=s,
    )
    generators.append(g)

print('GENERATING INDIVIDUALS\n******')
for g in generators:
    generated = g.generate(Config.INIT_INDIVIDUALS)
    assert None not in generated
    populations.append(generated)
    print('******')

print('STARTING EVOLUTION PROCESS\n******')
for s in itertools.product(*[populations, ext_strat, mut_strat, cross_strat]):
    print(s)
    population, es, ms, cs = s
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
        print('***')

    best_individuals.append(pool.best)

best_individuals.sort(key=lambda i: i.fitness)
best = best_individuals[-1]
best = Config.add_meta(best)
print(f'Fitness: {best.fitness}')
for k, v in best.meta.items():
    print(f'{k} -- {v}')

write_output(best, "output.txt")
