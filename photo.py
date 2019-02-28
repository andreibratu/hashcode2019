class Photo:

    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = tags

    def __str__(self):
        return str(self.id)
