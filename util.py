from typing import List
from photo import Photo
from individual import Individual


def read_input(file_name: str) -> List[Photo]:
    """Read problem input from textfile and return Photo objects."""

    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        n = int(lines[0])
        lines.pop(0)
        photos = []
        idx = 0
        for line in lines:
            elements = line.split(" ")
            orientation = elements[0]
            how_many_tags = int(elements[1])
            if how_many_tags > 0:
                tags = elements[2:]
            photos.append(Photo(id=idx, orientation=orientation, tags=tags))
            idx += 1
        return photos


def write_output(individual: Individual, file_name: str):
    """Write the solution in output file."""

    with open(file_name, 'w') as f:
        f.write(len(individual.slides()))
        for slide in individual.slides():
            f.write(str(slide))
