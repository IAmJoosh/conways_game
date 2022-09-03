import numpy as np
HEIGHT = 5
WIDTH = 5
GRID_SIZE = HEIGHT, WIDTH
GRID = np.zeros(GRID_SIZE)
GRID[1,2] = 1
GRID[2,2] = 1
GRID[3,2] = 1

def count_north(row, col, count):
    count += GRID[row-1, col]

def count_south(row, col, count):
    count += GRID[row+1, col]

def count_west(row, col, count):
    count += GRID[row, col-1]

def count_east(row, col, count):
    count += GRID[row, col+1]

def count_nw(row, col, count):
    count += GRID[row-1, col-1]

def count_sw(row, col, count):
    count += GRID[row+1, col-1]

def count_ne(row, col, count):
    count += GRID[row-1, col+1]

def count_se(row, col, count):
    count += GRID[row+1, col+1]

def count_neighbours(cell):
    row = cell[0]
    col = cell[1]
    count = 0

    # Moore Neighbours
    # 8 surrounding cells

    # corner cells 'edge case'
    # top left corner
    if row == 0 and col == 0:
        count_east(row, col, count)
        count_se(row, col, count)
        count_south(row, col, count)
    
    # top right corner
    elif row == 0 and col == WIDTH-1:
        count_west(row, col, count)
        count_sw(row, col, count)
        count_south(row, col, count)

    # bottom left corner
    elif row == HEIGHT-1 and col == 0:
        count_north(row, col, count)
        count_ne(row, col, count)
        count_east(row, col, count)
    
    # bottom right corner
    elif row == HEIGHT-1 and col == WIDTH-1:
        count_west(row, col, count)
        count_nw(row, col, count)
        count_north(row, col, count)
    
    # border 'edge' cases
    elif col == 0:
        # dont count any on left
        count_north(row, col, count)
        count_ne(row, col, count)
        count_east(row, col, count)
        count_se(row, col, count)
        count_south(row, col, count)

    elif col == WIDTH-1:
        # dont count any on right
        count_north(row, col, count)
        count_nw(row, col, count)
        count_west(row, col, count)
        count_sw(row, col, count)
        count_south(row, col, count)

    elif row == 0:
        # dont count any on top
        count_west(row, col, count)
        count_sw(row, col, count)
        count_south(row, col, count)
        count_se(row, col, count)
        count_east(row, col, count)

    elif row == HEIGHT-1:
        # dont count any on bottom
        count_west(row, col, count)
        count_nw(row, col, count)
        count_north(row, col, count)
        count_ne(row, col, count)
        count_east(row, col, count)

if __name__ == '__main__':
    
    print(GRID)

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
    
    print(GRID)