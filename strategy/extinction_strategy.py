import random
from typing import List, Callable
from models.individual import Individual

from config import Config


# def no_remove(individuals: List[Individual]) -> List[Individual]:
#     """Keep entire population between GENERATIONS.
#
#     Leads to more diversity over time, might slow evolution in later stages.
#     """
#
#     return individuals


def rm_least_fit(individuals: List[Individual]) -> List[Individual]:
    """Remove lowest fit `percent` individuals from the population.

    Raises the overall fitness of the pool, might converge to a local optimum.
    """

    individuals.sort(key=lambda i: i.fitness)
    individuals = individuals[-1:-Config.INDIVIDUALS-1:-1]
    assert len(individuals) == Config.INDIVIDUALS
    return individuals

def rm_random(individuals: List[Individual]) -> List[Individual]:
    """Remove a random percent of the pool.

    Avoid local optimums at cost of longer convergence time.
    """

    individuals = random.sample(individuals, Config.INDIVIDUALS)
    return individuals
