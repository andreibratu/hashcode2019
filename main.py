import random
import itertools
import sys

from models.photo import Photo
from models.slide import Slide
from models.individual import Individual
from models.generator import Generator
from models.pool import Pool

from strategy.extinction_strategy import rm_least_fit
from strategy.mutation_strategy import random_mutation
from strategy.discard_strategy import keep_all

from config import Config
from util import read_input, write_output

# input_files = ['a_example.txt', 'b_lovely_landscapes.txt',
#                'c_memorable_moments.txt', 'd_pet_pictures.txt',
#                'e_shiny_selfies.txt']
input_files = [sys.argv[1]]

######
best_individuals = []
discard_strategies = [keep_all]
extinction_strategies = [rm_least_fit]
mutation_strategies = [random_mutation]
######

for input_file in input_files:
    print(f'INPUT: {input_file}')
    Generator.id = 0
    Pool.id = 0

    output_file = input_file[0] + '_output.txt'

    photos = read_input(input_file)
    generator = Generator(photos)

    population = [
        Individual(generator.get_slideshow())
        for _ in range(Config.INDIVIDUALS)
    ]
    for i in population:
        i.calculate_fitness()

    strategies = itertools.product(*[
        extinction_strategies,
        mutation_strategies,
    ])

    print('STARTING EVOLUTION PROCESS\n******')
    for s in strategies:
        es, ms = s
        print(es.__name__, ms.__name__)

        pool = Pool(
            population=population[:],
            extinction_strategy=es,
            mutation_strategy=ms,
        )

        for g in range(Config.GENERATIONS):
            random.seed(None)
            pool.evolve()
            pool.set_best_individual()
            bf = pool.population[-1].fitness
            print(f'POOL {pool.id} GENERATION {g} FITNESS {bf}')

        best_individuals.append(pool.best)

        best_individuals.sort(key=lambda i: i.fitness)
        best = best_individuals[-1]
        # best = Config.add_meta(best)

    write_output(best, output_file)
