import numpy as np
HEIGHT = 5
WIDTH = 5
GRID_SIZE = HEIGHT, WIDTH
GRID = np.zeros(GRID_SIZE)

def count_neighbours(cell):
    row = cell[0]
    col = cell[1]
    count = 0

    # Moore Neighbours
    # 8 surrounding cells
    if col == 0:
        # dont check any on left
        pass
    if col == WIDTH-1:
        # dont check any on right
        pass
    if row == 0:
        # dont check any on top
        pass
    if row == HEIGHT-1:
        # dont check any on bottom
        pass

if __name__ == '__main__':
    for row in range(HEIGHT):
        for col in range(WIDTH):

            if count_neighbours((row, col)) == 2:
                # do nothing
                pass

            if count_neighbours((row, col)) == 3:
                # make cell alive
                GRID[row, col] = 1

            else:
                # kill cell
                GRID[row, col] = 0