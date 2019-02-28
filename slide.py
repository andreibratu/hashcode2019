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
