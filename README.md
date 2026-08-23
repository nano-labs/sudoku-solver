# sudoku-solver
Sudoku is a logic-based, combinatorial number-placement puzzle. 

## Rules
In classic Sudoku, the objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contains all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which, for a well-posed puzzle, has a single solution.

## Usage
```python
sudoku = [
    # 1 2  3  4  5  6  7  8  9
    [5, 3, _, _, 7, _, _, _, _],  # 1
    [6, _, _, 1, 9, 5, _, _, _],  # 2
    [_, 9, 8, _, _, _, _, 6, _],  # 3
    [8, _, _, _, 6, _, _, _, 3],  # 4
    [4, _, _, 8, _, 3, _, _, 1],  # 5
    [7, _, _, _, 2, _, _, _, 6],  # 6
    [_, 6, _, _, _, _, 2, 8, _],  # 7
    [_, _, _, 4, 1, 9, _, _, 5],  # 8
    [_, _, _, _, 8, _, _, 7, 9],  # 9
]

s = SudokuSolver(sudoku)
s.print()
s.solve()
```

![Run](https://github.com/nano-labs/sudoku-solver/blob/main/imgs/sudoku-solver.gif)







> [!NOTE]  
> No AI was used to write this rubbish.