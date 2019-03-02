from typing import List, Callable, NewType
import random

from individual import Individual
from strategies import tuple_cross


class Pool:

    def __init__(self, population: List[Individual], cross_strategy: Callable,
                 mutation_strategy: Callable, extinction_strategy: Callable,
                 new_indiviuals_setting: int, die_individuals_setting: int,
                 mutation_prob: int):
        self.population = population
        self.cross_strategy = cross_strategy
        self.mutation_strategy = mutate_strategy
        self.extinction_strategy = extinction_strategy
        self.new_indiviuals_setting = new_indiviuals_setting
        self.die_individuals_setting = die_individuals_setting
        self.mutation_probability = mutation_prob
        self._total_fitness = 0
        self.calculate_population_fitness()


    def calculate_population_fitness(self):
        """Calculate population fitness and sort it ascendingly."""

        self._total_fitness = 0
        for i in self.population:
            i.calculate_fitness()
            self._total_fitness += i.fitness
        self.population.sort(key=lambda i: i.fitness)


    def get_best_individual(self) -> Individual:
        self.calculate_population_fitness()
        return self.population[-1]


    def select_individual(self) -> Individual:
        """Select individual with a bias towards fitness.

        We can imagine the total fitness of the population as a pie chart,
        where more fit individuals take a higher slice. Weselect a random
        radial in the pie chart, and iterate from the start of the chart,
        until we find it.
        """
        aim = random.randrange(0, self._total_fitness)
        seen_fitness = 0
        for i in pool:
            if seen_fitness >= aim:
                return i
            else:
                seen_fitness += i.fitness


    def evolve(self):
        offsprings = []

        for _ in range(self.new_indiviuals_setting):
            i1 = self.select_individual()
            i2 = self.select_individual()
            offspring = self.cross_strategy(i1, i2)
            offsprings.append(offspring)

        for i in self.population:
            if random.random() <= self.mutation_probability:
                i = self.mutation_strategy(i)

        individuals += offsprings

        self.calculate_population_fitness()

        for _ in range(self.die_individuals_setting):
            self.extinction_strategy(self.population)
