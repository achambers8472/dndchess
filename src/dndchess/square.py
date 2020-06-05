class Square:
    def __init__(self):
        self._piece = None

    def add(self, piece):
        if self._piece is not None:
            raise ValueError("Can't put another piece in the same square!")

        self._piece = piece

    def __str__(self):
        return "x" if self._piece is None else str(self._piece)
