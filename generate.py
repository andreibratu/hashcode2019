import random


def generate_photo_series(photos, how_many, discard_chance):
    pass
#     """Generate a pool of valid photo series.
#
#     A series is valid if there is an even number of photos in it and has not been generated yet.
#     Args:
#         photos (List[int]): List of photo ids
#         how_many (int): How many series are desired
#     Returns:
#         A list of valid photo series, represented as tuples by ids.
#     """
#
#     valid = 0
#     series = set()
#     good = []
#     while valid < how_many:
#         print(f'Generating series #{valid}')
#         candidate = []
#         for photo in photos:
#             if random.random() > discard_chance:
#                 # photo is not discarded
#                 candidate.append(photo)
#         vertical_photos_in_candidate = 0
#         for p in candidate:
#             print(p)
#         for photo in candidate:
#             if photo.orientation == "V":
#                 vertical_photos_in_candidate += 1
#         #vertical_photos_in_candidate = len([photo in candidate if photo.orientation == 'V'])
#         if vertical_photos_in_candidate % 2 == 0:
#             print([photo.id for photo in candidate])
#             print(series)
#             if tuple([photo.id for photo in candidate]) not in series:
#                 series.add(tuple([photo.id for photo in candidate]))
#                 good += candidate
#                 valid += 1
    #
    # return good


def generate_individual(series):
    """Generate random individual from photo serie.

    Args:
        serie (List[photo]): A serie of photos
    Returns:
        A list of tuples that represent a slide.
    """
    # print(series)

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
