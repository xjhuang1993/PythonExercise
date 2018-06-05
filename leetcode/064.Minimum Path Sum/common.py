"""
Accepted
"""


def func(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j != 0:
                grid[i][j] += grid[i][j - 1]
            elif i != 0 and j == 0:
                grid[i][j] += grid[i - 1][j]
            elif i != 0 and j != 0:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]


if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(func(grid))
