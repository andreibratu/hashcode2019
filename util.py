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
        for idx, l in enumerate(lines):
            orientation = l[0]
            how_many_tags = l[1]
            if how_many_tags > 0:
                tags = l[2:]
            photos.append(Photo(id=idx, orientation=orientation, tags=tags))
        return photos


def write_output(candidate):
    """
    Args:
        candidate (List[Slides]): A list of slides
    """

    with open('output.txt', 'w') as f:
        f.write(len(candidate))
        for slide in candidate:
            f.write(str(slide))
