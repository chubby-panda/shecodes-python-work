def add_column(grid):
    """Adds a new column to a grid. For each row, if there is an even
    number of X characters, a O is added to the row, otherwise a X is added
    to the row.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        The same grid, with a new column added.
    """
    for row in grid:
        x_counter = 0
        for item in row:
            if item == "X":
                x_counter += 1
        if x_counter%2 != 0:
            row.append("X")
        elif x_counter%2 == 0:
            row.append("O")
    return grid

def add_row(grid):
    """Adds a new row to a grid. For each column, if there is an even
    number of X characters, a O is added to the column, otherwise a X is added
    to the column.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        The same grid, with a new row added.
    """
    last_row = []
    columns = list(zip(*grid))
    for column in columns:
        x_counter = 0
        for item in column:
            if item == "X":
                x_counter += 1
        if x_counter%2 != 0:
            last_row.append("X")
        elif x_counter%2 == 0:
            last_row.append("O")
    grid.append(last_row)
    return grid


def increase_grid_size(grid):
    """Adds a new column and row to a grid.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        The same grid, with a new row and column added.
    """
    add_column(grid)
    add_row(grid)
    return grid

def flip_card(x_pos, y_pos, grid):
    """Prompts the user to choose a cell to swap from X to O (or vice versa).

    Arguments:
        x_pos: An integer representing the x coordinate of the cell.
        y_pos: An integer representing the y coordinate of the cell.
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        The same grid, with a cell switched.
    """
    card = grid[y_pos][x_pos]
    if card == "X":
        grid[y_pos][x_pos] = "O"
    elif card == "O":
        grid[y_pos][x_pos] = "X"
    return grid

def find_flipped_card(grid):
    """Prompts the user to choose a cell to swap from X to O (or vice versa).

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.
    
    Returns:
        A list containing the coordinates of the cell with the flipped card.
        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = (0, 1)
            b = (1, 1)
            c = (0, 0)
            d = (1, 0)
    """
    pass

def print_grid(grid):
    for row in grid:
        print(row)

if __name__ == "__main__":
    grid = [
        ["X","O","X","X","X"],
        ["X","X","O","O","O"],
        ["X","O","X","O","X"],
        ["O","X","X","X","X"],
        ["X","O","O","X","X"]
    ]
    print((increase_grid_size(grid)))
    print("Pick a cell to flip")
    x_pos = int(input("Cell x pos: "))
    y_pos = int(input("Cell y pos: "))
    grid = flip_card(x_pos, y_pos, grid)