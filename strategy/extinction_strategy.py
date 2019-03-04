from typing import List, Callable
from models.individual import Individual


def no_remove() -> Callable:
    """Keep entire population between generations.

    Leads to more diversity over time, might slow evolution in later stages.
    """

    def f(individuals: List[Individual]) -> List[Individual]:
        return individuals


def rm_least_fit(percent: float) -> Callable:
    """Remove lowest fit `percent` individuals from the population.

    Raises the overall fitness of the pool, might converge to a local optimum.
    """

    def f(individuals: List[Individual]) -> List[Individual]:
        individuals.sort(lambda i: i.fitness)
        to_remove = int(len(individuals)*percent)
        return individuals[to_remove+1:]

    assert 0 < percent < 1
    return f


def rm_random(percent: float) -> Callable:
    """Remove a random percent of the pool.

    Avoid local optimums at cost of longer convergence time.
    """

    def f(individuals: List[Individual]) -> List[Individual]:
        how_many_left = len(individuals) - int(len(individuals) * percent)
        return random.sample(individuals, how_many_left)

    assert 0 < percent < 1
    return f
