from typing import Tuple

import numpy as np

from .square import Square


class Board:
    def __init__(self, shape):
        self._grid = np.empty(shape=shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                self._grid[i, j] = Square()

    @property
    def shape(self):
        return self._grid.shape

    def __getitem__(self, position):
        return self._grid[position]

    def __str__(self):
        disp = np.full(self.shape, " ")
        for i in range(self._grid.shape[0]):
            for j in range(self._grid.shape[1]):
                disp[i, j] = str(self[i, j])
        s = "\n".join(" ".join(row) for row in disp)
        return s
