import random
from typing import List, Callable
from models.individual import Individual

from config import Config


def no_remove(individuals: List[Individual]) -> List[Individual]:
    """Keep entire population between generations.

    Leads to more diversity over time, might slow evolution in later stages.
    """

    return individuals


def rm_least_fit(individuals: List[Individual]) -> List[Individual]:
    """Remove lowest fit `percent` individuals from the population.

    Raises the overall fitness of the pool, might converge to a local optimum.
    """

    assert 0 < Config.EXTN_PER < 1

    individuals.sort(key=lambda i: i.fitness)
    to_remove = int(len(individuals) * Config.EXTN_PER)
    return individuals[to_remove+1:]


def rm_random(individuals: List[Individual]) -> List[Individual]:
    """Remove a random percent of the pool.

    Avoid local optimums at cost of longer convergence time.
    """

    assert 0 < Config.EXTN_PER < 1

    how_many_left = len(individuals) - int(len(individuals) * Config.EXTN_PER)
    return random.sample(individuals, how_many_left)
