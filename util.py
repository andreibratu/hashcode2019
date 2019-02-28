class Photo:

    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = tags


class Slide:

    def __init__(self, photo1, photo2 = None):
        if photo2 is not None:
            assert photo1.orientation == 'V' and photo2.orientation == 'V'
        self.photo1 = photo1
        self.photo2 = photo2

    def __str__(self):
        if photo2 is None:
            return str(self.photo1.id)
        else:
            return f'{photo1.id} {photo2.id}'


def calculate_interesting_factor(slide1, slide2):
    """
    Args:
        slide1 (Slide)
        slide2 (Slide)
    Returns:
        In int representing interesting factor between two slides.
    """
    photo1 = set(slide1.tags)
    photo2 = set(slide2.tags)

    # Set operations return a new set
    only_photo1 = len(photo1-photo2)
    only_photo2 = len(photo2-photo1)
    in_both_photos = len(photo1&photo2)

    return min(min(unique_photo1, unique_photo2), in_both_photos)


def read_input(file_name):
    """
    Args:
        file_name (str): The filename, in the same path as the script
    Returns:
        A list of Photo objects.
    """

    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        n = int(lines[0])
        lines.pop()
        photos = []
        for idx, l in enumerate(lines_photos):
            orientation = l[0]
            how_many_tags = l[1]
            if how_many_tags > 0:
                tags = l[2:]
            photos.append(Photo(id=idx, orientation=orientation, tags=tags))
        return photos
