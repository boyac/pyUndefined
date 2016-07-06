neighbors = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) # grid (row, col)

def count_neighbours(grid, row, col):
    count = 0
    for diff in neighbors:
    # iterate though row & col of neighbors
        n_row = row + diff[0]
        n_col = col + diff[1]
        if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]):
            # what is len(grid[n_row])?
            if grid[n_row][n_col]:
                count += 1
    return count
