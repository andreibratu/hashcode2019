import random


def generate_photo_series(photos, how_many, discard_chance):
    """Generate a pool of valid photo series.

    A series is valid if there is an even number of photos in it and has not been generated yet.
    Args:
        photos (List[int]): List of photo ids
        how_many (int): How many series are desired
    Returns:
        A list of valid photo series, represented as tuples by ids.
    """

    valid = 0
    series = set()
    while valid < how_many:
        candidate = []
        for photo in photos:
            if random.random() > discard_chance:
            # Photo is not discarded
            candidate.append(photo)
        vertical_photos_in_candidate = len([photo in candidate if photo.orientation == 'V'])
        if vertical_photos_in_candidate % 2 == 0 and tuple(candidate) not in series:
            series.append(tuple(candidate))

    return list(series)


def generate_individual(serie):
    """Generate random individual from photo serie.

    Args:
        serie (List[Photo]): A serie of photos
    Returns:
        A list of tuples that represent a slide.
    """
    slides = [(p.id, None) for p in series if p.orientation == 'H']
    vertical_photos = [p.id for p in series if p.orientation == 'V']
    l = len(vertical_photos)

    while l != 0:
        v_photo1, v_photo2 = random.sample(vertical_photos, 2)
        vertical_photos.remove(v_photo1)
        vertical_photos.remove(v_photo2)
        slides.append((v_photo1, v_photo2))
        l -= 2

    return slides
