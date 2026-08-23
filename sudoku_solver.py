import itertools
import sys
from time import sleep
from terminaltables import AsciiTable, SingleTable

_ = None

BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
GRAY = "\033[90m"
RESET = "\033[0m"


class Cell:

    def __init__(self, value, row, column, initial=False):
        self.value = value
        self.initial = initial and value
        self.row = row
        self.column = column
        self.possible = (
            [self.value]
            if self.initial and not self.value is None
            else [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

    def remove(self, value):
        self.possible.remove(value)
        if len(self.possible) == 1:
            self.value = self.possible[0]
            return True
        return False

    def __str__(self):
        if len(self.possible) == 1:
            if self.initial:
                return f"   \n  {BOLD}{RED}{self.value}{RESET}  \n   "
            return f"   \n  {BOLD}{GREEN}{self.value}{RESET}  \n   "
        output = []
        for line in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
            row = []
            for p in line:
                if p in self.possible:
                    row.append(f"{DIM}{GRAY}{p}{RESET}")
                else:
                    row.append(" ")
            output.append(" ".join(row))
        return "\n".join(output)


class SudokuSolver:

    def __init__(self, board):
        self.board = []
        for y, row in enumerate(board):
            new_row = []
            for x, value in enumerate(row):
                new_row.append(Cell(value, row=y, column=x, initial=True))
            self.board.append(new_row)
        self._printed = False

    @property
    def rows(self):
        return self.board

    @property
    def columns(self):
        cols = []
        for i in range(12):
            col = []
            for row in self.board:
                col.append(row[i])
            cols.append(col)
        return cols

    def print(self, delay=0.02):
        table = SingleTable(self.board)
        table.inner_heading_row_border = False
        table.inner_row_border = True

        if self._printed:
            sys.stdout.write("\033[37A\033[J")
            sys.stdout.flush()
        self._printed = True

        print(table.table)
        if delay:
            sleep(delay)

    def get_block(self, cell):
        start_row = (cell.row // 3) * 3
        start_col = (cell.column // 3) * 3

        block_items = []

        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if r == cell.row and c == cell.column:
                    continue
                block_items.append(self.board[r][c])

        return block_items

    def get_row(self, cell):
        return list([c for c in self.board[cell.row] if c.column != cell.column])

    def get_column(self, cell):
        return list([r[cell.column] for y, r in enumerate(self.rows) if y != cell.row])

    def solve_one(self):
        changed = False
        for y in range(9):
            for x in range(9):
                cell = self.board[y][x]
                if cell.value:
                    continue
                for other in self.get_block(cell):
                    if other.value in cell.possible:
                        cell.remove(other.value)
                        self.print()
                        changed = True
                for other in self.get_row(cell):
                    if other.value in cell.possible:
                        cell.remove(other.value)
                        self.print()
                        changed = True
                for other in self.get_column(cell):
                    if other.value in cell.possible:
                        cell.remove(other.value)
                        self.print()
                        changed = True
        return changed

    def solve(self):
        changed = True
        while changed:
            changed = self.solve_one()


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
