from classes import Photo, Slide, Individual
from util import read_input, write_output

# Hyperparameters
GENERATIONS = 1000
TUPLE_SIZE_BOUND = 5
SWAP_SLIDES_CHANCE_BOUND = 0.2
DISCARD_PHOTO_CHANCE = 0.1
SERIES = 50
SLIDES_FROM_SERIE = 10000
POPULATION = SERIES * SLIDES_FROM_SERIE
POOL = []

photos = read_input("a_example.txt")
series = generate_photo_series([p.id for p in photos], SERIES, DISCARD_PHOTO_CHANCE_BOUND)

for s in series:
    for s in range(SLIDES_FROM_SERIE):
        s =
        individual = generate_individual(s)
        print(individual)
        individual = [Slide(p1, p2) for p1, p2 in individual]
        POOL.append(individual)
