import random
from functools import reduce
from queue import Queue
from threading import Thread
from typing import List, Callable, Tuple
from numpy.random import choice
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


    def select_parents(self) -> Tuple[Individual, Individual]:
        """Select 2 individuals with a bias towards fitness."""

        tf = reduce(lambda acc, f: acc+f, [i.fitness for i in self.population])
        prob = [i.fitness/tf for i in self.population]
        parents = choice(a=self.population, replace=False, size=(1, 2), p=prob)
        return parents[0] #First row of the 1x2 numpy array


    def evolve(self):
        def create_offspring(q, result):
            while not q.empty():
                idx = q.get()

                i1, i2 = self.select_parents()
                # print(f'POOL {self.id} OFFSPRING {idx} <- {i1} x {i2}')
                offspring = self.cross_strategy(i1, i2)
                offspring.meta = i1.meta
                result[idx] = offspring

                q.task_done()
            return True

        offsprings = [None for _ in range(Config.OFFSPRING)]
        work_q = Queue(maxsize=0)
        num_threads = min(50, Config.OFFSPRING)

        for i in range(Config.OFFSPRING):
            work_q.put(i)

        for i in range(num_threads):
            worker = Thread(target=create_offspring, args=[work_q, offsprings])
            worker.setDaemon(True)
            worker.start()

        work_q.join()

        assert None not in offsprings

        for i in self.population:
            if random.random() <= Config.MUTATATION_PROB:
                i = self.mutation_strategy(i)
                i.calculate_fitness()

        self.population += offsprings
        self.population = self.extinction_strategy(self.population)
