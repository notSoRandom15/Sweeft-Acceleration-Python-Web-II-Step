def bomber_man(n, grid):
    rows, cols = len(grid), len(grid[0])

    grid = [list(row) for row in grid]

    for t in range(n):
        if t % 2 == 0:

            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 'O':
                        grid[i][j] = '.'

                        if i > 0:
                            grid[i-1][j] = '.'
                        if i < rows - 1:
                            grid[i+1][j] = '.'
                        if j > 0:
                            grid[i][j-1] = '.'
                        if j < cols - 1:
                            grid[i][j+1] = '.'
        else:

            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == '.':
                        grid[i][j] = 'O'

    output = ["".join(row) for row in grid]

    return output                    


n = 3
grid = [
    '. . . . . . .',
    '. . . O . . .',
    '. . . . O . .',
    '. . . . . . .',
    'O O . . . . .',
    'O O . . . . .'
]

print(bomber_man(n, grid))