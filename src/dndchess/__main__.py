import sys

from .board import Board
from .piece import Piece


def main(args):
    king = Piece("K")
    board = Board((8, 8))
    board[2, 4].add(king)
    print(board)


if __name__ == "__main__":
    exit(main(sys.argv[1:]))
