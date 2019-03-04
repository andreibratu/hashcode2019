from models.individual import Individual

def no_mutation(i: Individual):
    return i


def swap_photos_in_slide(i: Individual):
    # TODO
    while True:
        idx = random.randrange(0, len(i.slides)-1)
        if i.slides[idx].photo2 is not None:
            break
    i.slides[idx].photo1, i.slides[idx].photo2 = \
        i.slides[idx].photo2, i.slides[idx].photo1
