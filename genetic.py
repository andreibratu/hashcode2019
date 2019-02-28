from classes import Photo, Slide, Individual
from util import read_input, write_output

# Hyperparameters
GENERATIONS = 1000
TUPLE_SIZE_BOUND = 5
SWAP_SLIDES_MUTATION_CHANCE_BOUND = 0.2
DISCARD_PHOTO_CHANCE = 0.1
SERIES = 50
SLIDES_FROM_SERIE = 10000
POPULATION = SERIES * SLIDES_FROM_SERIE
POOL = []

photos = read_input("a_example.txt")
series = generate_photo_series([p.id for p in photos], SERIES, DISCARD_PHOTO_CHANCE_BOUND)

for s in series:
    for s in range(SLIDES_FROM_SERIE):
        for i in range(SLIDES_FROM_SERIE):
            individual = generate_individual(s)
            print(individual)
            # Build the slide back from ids
            slides = []
            for idx1, idx2 in individual:
                p1 = photos[idx1]
                if p2 is not None:
                    p2 = photos[idx2]
                s = Slide(p1, p2)
                slides.append(s)

            individual = Individual(slide)
            POOL.append(individual)

print(POOL)
