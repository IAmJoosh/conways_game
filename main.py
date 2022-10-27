#!.\venv\Scripts\python
import numpy as np
from time import sleep

HEIGHT = 6
WIDTH = 6
GRID_SIZE = HEIGHT, WIDTH
GRID = np.zeros(GRID_SIZE)
GRID[2, 2] = 1
GRID[2, 3] = 1
GRID[2, 4] = 1
GRID[3, 1] = 1
GRID[3, 2] = 1
GRID[3, 3] = 1


def reset_cursor(height: int, width: int):
    print(f"\033[{height}A", end="")
    print(f"\033[{width}D", end="")


def is_in_bounds(height: int, width: int, row: int, col: int) -> bool:
    if 0 <= row <= height - 1 and 0 <= col <= width - 1:
        return True
    return False


def count_neighbours(row: int, col: int) -> int:
    # Moore Neighbours
    # 8 surrounding cells
    count = 0
    for row_delta in range(-1, 2):
        for col_delta in range(-1, 2):
            if row_delta == 0 and col_delta == 0:
                pass
            elif is_in_bounds(HEIGHT, WIDTH, row + row_delta, col + col_delta):
                count += GRID[row + row_delta, col + col_delta]
    return count


if __name__ == "__main__":

    # print(GRID)
    while True:
        print(GRID, flush=True)
        new_grid = {}
        for row in range(HEIGHT):
            for col in range(WIDTH):

                if count_neighbours(row, col) == 2:
                    # do nothing
                    pass

                elif count_neighbours(row, col) == 3:
                    # make cell alive
                    new_grid[(row, col)] = 1

                else:
                    # kill cell
                    new_grid[(row, col)] = 0

        for cell, state in new_grid.items():
            GRID[cell[0], cell[1]] = state

        sleep(0.5)
        reset_cursor(HEIGHT, WIDTH)
