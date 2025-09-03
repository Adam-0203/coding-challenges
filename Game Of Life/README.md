# Game of Life

This Python project implements a basic version of **Conway’s Game of Life**, a cellular automaton that simulates the evolution of a grid of cells over time based on simple rules.

## How it Works

- The grid is represented by a 2D list `Mat`, where:
  - `0` → dead cell
  - `1` → alive cell
- Each cell evolves according to its **live neighbors**:
  1. A dead cell with exactly **3 live neighbors** becomes alive (birth).
  2. A live cell with **2 or 3 live neighbors** stays alive (survival).
  3. A live cell with fewer than 2 or more than 3 live neighbors dies (underpopulation or overpopulation).

- The function `voisin_vivant(Mat, i, j)` counts the number of live neighbors of a given cell.
- The function `nouveau(Mat, i, j)` calculates the next state of a cell based on the rules.
- The function `algo(Mat, step)` simulates the grid for a given number of steps and prints each generation.

## Example

```python
Mat = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

algo(Mat, 4)
