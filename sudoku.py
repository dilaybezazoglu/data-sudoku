# pylint: disable=missing-docstring


def is_valid_group(group):
    return set(group) == set(range(1, 10))
def rows_are_valid(grid):
    for row in grid:
        if not is_valid_group(row):
            return False
    return True

def columns_are_valid(grid):
    for col_index in range(9):
        column = []
        for row_index in range(9):
            column.append(grid[row_index][col_index])

        if not is_valid_group(column):
            return False

    return True
def boxes_are_valid(grid):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    box.append(grid[row][col])

            if not is_valid_group(box):
                return False

    return True
def sudoku_validator(grid):
    return (
        rows_are_valid(grid)
        and columns_are_valid(grid)
        and boxes_are_valid(grid)
    )

