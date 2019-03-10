from random import random, sample
from numpy.random import choice
from functools import reduce
from queue import Queue
from threading import Thread
from typing import List, Callable, Tuple
from models.individual import Individual
from config import Config


class Pool:

    id = 0

    def __init__(self, population: List[Individual],
                 mutation_strategy: Callable,
                 extinction_strategy: Callable):
        self.id = Pool.id
        self.population = population
        self.mutation_strategy = mutation_strategy
        self.extinction_strategy = extinction_strategy
        self.best = None

        Pool.id += 1


    def set_best_individual(self):
        self.population.sort(key=lambda i: i.fitness)
        if self.best is None or \
           self.population[-1].fitness > self.best.fitness:
           self.best = self.population[-1]


    def select_parent(self) -> Individual:
        """Select individual with bias towards fitness."""

        population_fitness = [i.fitness for i in self.population]
        tf = reduce(lambda acc, f: acc+f, population_fitness)
        p = [i.fitness/tf for i in self.population]
        return choice(a=self.population, p=p)


    def evolve(self):
        def create_offspring(q, result):
            while not q.empty():
                idx = q.get()

                p = self.select_parent()
                offspring = Individual(p.slides[:])
                best = None

                for _ in range(Config.OFFSPRING_MUTATIONS):
                    offspring = self.mutation_strategy(offspring)
                    offspring.calculate_fitness()
                    if best is None or offspring.fitness > best.fitness:
                        best = offspring

                result[idx] = offspring
                q.task_done()

            return True

        offsprings = [None for _ in range(Config.OFFSPRINGS)]
        work_q = Queue(maxsize=0)
        num_threads = min(50, Config.OFFSPRINGS)

        for i in range(Config.OFFSPRINGS):
            work_q.put(i)

        for i in range(num_threads):
            worker = Thread(target=create_offspring, args=[work_q, offsprings])
            worker.setDaemon(True)
            worker.start()

        work_q.join()

        self.population += offsprings
        self.population = self.extinction_strategy(self.population)
