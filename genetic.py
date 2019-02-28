from classes import Photo, Slide, Individual
from util import read_input, write_output
import random

############# Hypers #############
GENERATIONS = 1000
NEW_INDIVIDUALS = 100
TUPLE_SIZE_BOUND = 5
SWAP_SLIDES_MUTATION_CHANCE_BOUND = 0.2
DISCARD_PHOTO_CHANCE = 0
SERIES = 5
SLIDES_FROM_SERIE = 3
POOL = []
BEST_CANDIDATES = []
random.seed(None)


############# AUX #############
def select_individual(pool, total_fitnesss):
    """Select individuals with a bias towards more fit ones"""
    aim = random.randrange(0, total_fitness)
    seen_fitness = 0
    for i in pool:
        if seen_fitness >= aim:
            return i
        else:
            seen_fitness += i.fitness


def generate_offspring(i1, i2, tuple_size):
    """Cross two individuals."""

    flag_select_first = True
    new_individual = []
    last_index = 0
    for idx in range(0, len(i1), tuple_size):
        if flag_select_first:
            new_individual += i1[idx:idx+tuple_size+1]
        else:
            new_individual += i2[idx:idx+tuple_size+1]
        flag_select_first = not flag_select_first
        last_index = idx

    if len(new_individual) < len(i1):
        if flag_select_first:
            new_individual += i1[last_index:]
        else:
            new_individual += i2[last_index:]

    return new_individual


############# MAIN LOOP #############
photos = read_input("a_example.txt")
series = generate_photo_series([p.id for p in photos], SERIES, DISCARD_PHOTO_CHANCE)

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


for tuple_size in range(5, TUPLE_SIZE_BOUND+1):
    pool = POOL[:]
    print(f'TUPLE SIZE {tuple_size}\n******')
    for g in range(GENERATIONS):
        print(f'Generation {g}')
        total_fitness = 0
        for i in pool:
            i.calculate_fitness()
            total_fitness += i.fitness
        # Create offsprings
        for _ in range(NEW_INDIVIDUALS):
            i1 = select_individual(pool, total_fitness)
            i2 = select_individual(pool, total_fitness)
            pool += generate_offspring(i1, i2, tuple_size)
    sort(pool, key=lamba i: i.fitness)
    BEST_CANDIDATES.append(pool[-1])
    print('************************')

sort(BEST_CANDIDATES, key=lamba i: i.fitness)
write_output(BEST_CANDIDATES[-1])
