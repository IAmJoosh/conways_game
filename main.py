import numpy as np
from time import sleep
from os import system

HEIGHT = 6
WIDTH = 6
GRID_SIZE = HEIGHT, WIDTH
GRID = np.zeros(GRID_SIZE)
GRID[2,2] = 1
GRID[2,3] = 1
GRID[2,4] = 1
GRID[3,1] = 1
GRID[3,2] = 1
GRID[3,3] = 1

def count_north(row, col):
    return GRID[row-1, col]

def count_south(row, col):
    return GRID[row+1, col]

def count_west(row, col):
    return GRID[row, col-1]

def count_east(row, col):
    return GRID[row, col+1]

def count_nw(row, col):
    return GRID[row-1, col-1]

def count_sw(row, col):
    return GRID[row+1, col-1]

def count_ne(row, col):
    return GRID[row-1, col+1]

def count_se(row, col):
    return GRID[row+1, col+1]

def count_neighbours(row, col):
    count = 0

    # Moore Neighbours
    # 8 surrounding cells

    # corner cells 'edge case'
    # top left corner
    if row == 0 and col == 0:
        count += count_east(row, col)
        count += count_se(row, col)
        count += count_south(row, col)
    
    # top right corner
    elif row == 0 and col == WIDTH-1:
        count += count_west(row, col)
        count += count_sw(row, col)
        count += count_south(row, col)

    # bottom left corner
    elif row == HEIGHT-1 and col == 0:
        count += count_north(row, col)
        count += count_ne(row, col)
        count += count_east(row, col)
    
    # bottom right corner
    elif row == HEIGHT-1 and col == WIDTH-1:
        count += count_west(row, col)
        count += count_nw(row, col)
        count += count_north(row, col)
    
    # border 'edge' cases
    elif col == 0:
        # dont count any on left
        count += count_north(row, col)
        count += count_ne(row, col)
        count += count_east(row, col)
        count += count_se(row, col)
        count += count_south(row, col)

    elif col == WIDTH-1:
        # dont count any on right
        count += count_north(row, col)
        count += count_nw(row, col)
        count += count_west(row, col)
        count += count_sw(row, col)
        count += count_south(row, col)

    elif row == 0:
        # dont count any on top
        count += count_west(row, col)
        count += count_sw(row, col)
        count += count_south(row, col)
        count += count_se(row, col)
        count += count_east(row, col)

    elif row == HEIGHT-1:
        # dont count any on bottom
        count += count_west(row, col)
        count += count_nw(row, col)
        count += count_north(row, col)
        count += count_ne(row, col)
        count += count_east(row, col)

    else:
        # count all 8
        count += count_west(row, col)
        count += count_nw(row, col)
        count += count_north(row, col)
        count += count_ne(row, col)
        count += count_east(row, col)
        count += count_se(row, col)
        count += count_south(row, col)
        count += count_sw(row, col)

    return count

if __name__ == '__main__':
    
    # print(GRID)
    while True:
        print(GRID, flush=True)
        to_live = []
        to_die = []
        for row in range(HEIGHT):
            for col in range(WIDTH):

                if count_neighbours(row, col) == 2:
                    # do nothing
                    pass

                elif count_neighbours(row, col) == 3:
                    # make cell alive
                    to_live.append((row, col))

                else:
                    # kill cell
                    to_die.append((row, col))
        
        for life in to_live:
            GRID[life[0], life[1]] = 1
        
        for death in to_die:
            GRID[death[0], death[1]] = 0

        sleep(0.5)
        system("clear") #Could use escape sequences for this to repostion cursor instead of using system clear or cls