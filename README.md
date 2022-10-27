# Conway's Game of Life

Conway's game of life is a game created by John Conway

The game consists of a grid of cells that are either alive or dead.
I have chosen to represent living cells as a 1 and dead cells as a 0.

Every 'turn' of the game, the cells in the grid are changed based on a set of rules.
The rules are based on the number of living neighbours that a cell has.
The neighbours of a cell refer to the eight surrounding cells (Moore Neighbourhood).
Some version of the game may use the 4 neighbours on each cardinal point of a cell (Von Neumann Neighbourhood).

The rules:

1. If number of living neighbours is 2, the cell remains as is.

2. If the the number of living neighbours is 3, the cell becomes or stay alive.

3. If neither rule 1 or rule 2 is true, we make sure the cell is dead.

## Author: Joshua Whittaker

## Date: October 27th, 2022
