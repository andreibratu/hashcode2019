import random
from functools import reduce
from typing import List, Callable, NewType
from models.individual import Individual
from config import Config


class Pool:

    id = 0

    def __init__(self, population: List[Individual], cross_strategy: Callable,
                 mutation_strategy: Callable, extinction_strategy: Callable):
        self.population = population
        self.cross_strategy = cross_strategy
        self.mutation_strategy = mutation_strategy
        self.extinction_strategy = extinction_strategy
        self.id = Pool.id
        Pool.id += 1
        self.best = None
        assert None not in self.population


    def set_best_individual(self):
        self.population.sort(key=lambda i: i.fitness)
        if self.best is None or \
           self.population[-1].fitness > self.best.fitness:
           self.best = self.population[-1]
           assert hasattr(self.best, 'meta')
           assert 'discard' in self.best.meta
           self.best.meta.update({
            'pool_id': self.id,
            'cross': self.cross_strategy.__name__,
            'mutation': self.mutation_strategy.__name__,
            'extinction': self.extinction_strategy.__name__
           })


    def select_individual(self) -> Individual:
        """Select individual with a bias towards fitness.

        We can imagine the total fitness of the population as a pie chart,
        where more fit individuals take a higher slice. Weselect a random
        radial in the pie chart, and iterate from the start of the chart,
        until we find it.
        """

        tf = reduce(lambda acc, f: acc+f, [i.fitness for i in self.population])
        aim = random.randrange(0, tf)
        seen_fitness = 0
        for i in self.population:
            seen_fitness += i.fitness
            if seen_fitness >= aim:
                return i


    def evolve(self):
        offsprings = []

        for _ in range(Config.OFFSPRING):
            i1 = self.select_individual()
            i2 = self.select_individual()
            print(f'POOL {self.id} OFFSPRING {_} <- {i1} x {i2}')
            assert i1 is not None and i2 is not None
            offspring = self.cross_strategy(i1, i2)
            offspring.meta = i1.meta
            offsprings.append(offspring)

        for i in self.population:
            if random.random() <= Config.MUTATATION_PROB:
                i = self.mutation_strategy(i)
                i.calculate_fitness()

        self.population += offsprings
        self.population = self.extinction_strategy(self.population)
