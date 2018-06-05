"""
Accepted
"""


def func(matrix):
    row = len(matrix)
    if not row:
        return
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                for tmp in range(row):
                    if matrix[tmp][j] != 0:
                        matrix[tmp][j] = 'a'
                for tmp in range(col):
                    if matrix[i][tmp] != 0:
                        matrix[i][tmp] = 'a'

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 'a':
                matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [
        [1, 1, 1],
        [0, 1, 1],
        [1, 1, 1]
    ]
    func(matrix)
    print(matrix)
