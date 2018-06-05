"""
Accepted
"""


def func(matrix, target):
    row = len(matrix)
    if not row:
        return
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == target:
                return True
    return False


if __name__ == "__main__":
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    print(func(matrix, target))
