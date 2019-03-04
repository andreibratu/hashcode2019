import random
from functools import reduce
from typing import List, Callable, NewType
from models.individual import Individual
from config import Config


class Pool:

    def __init__(self, population: List[Individual], cross_strategy: Callable,
                 mutation_strategy: Callable, extinction_strategy: Callable,
                 idx: int):
        self.population = population
        self.cross_strategy = cross_strategy
        self.mutation_strategy = mutation_strategy
        self.extinction_strategy = extinction_strategy
        self.idx = idx
        self.best = None
        assert None not in self.population


    def set_best_individual(self):
        self.population.sort(key=lambda i: i.fitness)
        if self.best is None or \
           self.population[-1].fitness > self.best.fitness:
           self.best = self.population[-1]


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
            print(f'POOL {self.idx+1} OFFSPRING {_+1}/{Config.OFFSPRING}')
            i1 = self.select_individual()
            i2 = self.select_individual()
            assert i1 is not None and i2 is not None
            offspring = self.cross_strategy()(i1, i2)
            offsprings.append(offspring)

        for i in self.population:
            if random.random() <= Config.MUTATATION_PROB:
                i = self.mutation_strategy(i)
                i.calculate_fitness()

        self.population += offsprings
        self.population = self.extinction_strategy(self.population)
        self.set_best_individual()
