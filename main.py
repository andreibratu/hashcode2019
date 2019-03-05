import random
import itertools

from models.photo import Photo
from models.slide import Slide
from models.individual import Individual
from models.generator import Generator
from models.pool import Pool

from strategy.discard_strategy import keep_all, discard_outlier, discard_random
from strategy.cross_strategy import slice_cross, adaptive_slice_cross
from strategy.mutation_strategy import no_mutation, swap_photos_slide, \
                                       swap_slides, random_mutate
from strategy.extinction_strategy import rm_least_fit, rm_random

from config import Config
from util import read_input, write_output

discard_strategy = [keep_all, discard_outlier, discard_random]
cross_strat = [adaptive_slice_cross, slice_cross]
extinction_strategy = [rm_least_fit]
mutation_strategy = [random_mutate]
input_files = ['a_example.txt', 'b_lovely_landscapes.txt',
               'c_memorable_moments.txt', 'd_pet_pictures.txt',
               'e_shiny_selfies.txt']

Config.GENERATORS = len(discard_strategy)

######
generators = []
pops = []
pools = []
best_individuals = []
######

for input_file in input_files:
    print(f'INPUT: {input_file}')
    Generator.id = 0
    Pool.id = 0

    output_file = input_file[0] + '_output.txt'
    photos = read_input(input_file)

    for s in discard_strategy:
        g = Generator(
            photos=photos,
            discard_strategy=s,
        )
        generators.append(g)

    print('GENERATING INDIVIDUALS\n******')
    for g in generators:
        generated = g.generate(Config.INDIVIDUALS)
        assert None not in generated
        pops.append(generated)
        print('******')

    print('STARTING EVOLUTION PROCESS\n******')
    strategies = itertools.product(
        *[pops, extinction_strategy, mutation_strategy, cross_strat]
    )
    how_many_s = len(pops) * len(extinction_strategy) * \
                 len(mutation_strategy)*len(cross_strat)

    for strategy in strategies:
        population, es, ms, cs = s
        print(es.__name__, ms.__name__, cs.__name__)
        Config.CURR_GENERATION = 0

        pool = Pool(
            population=population[:],
            extinction_strategy=es,
            mutation_strategy=ms,
            cross_strategy=cs,
        )

        for g in range(Config.GENERATIONS):
            random.seed(None)
            Config.CURR_GENERATION += 1
            pool.evolve()
            pool.set_best_individual()
            bf = pool.population[-1].fitness
            print(f'POOL {pool.id}/{how_many_s-1} GENERATION {g} FITNESS {bf}')

        best_individuals.append(pool.best)

    best_individuals.sort(key=lambda i: i.fitness)
    best = best_individuals[-1]
    best = Config.add_meta(best)
    print(f'\nFitness -- {best.fitness}')
    for k, v in best.meta.items():
        print(f'{k} -- {v}')
    print('\nWRITING OUTPUT...')
    write_output(best, output_file)
