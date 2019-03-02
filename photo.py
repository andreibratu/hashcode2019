from typing import List

class Photo:

    def __init__(self, id: int, orientation: str, tags: List[str]):
        self.id = id
        self.orientation = orientation
        self.tags = tags

    def __str__(self):
        return str(self.id)
