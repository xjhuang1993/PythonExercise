"""
Accepted
顺时针转九十度，就是先对角翻转，再水平翻转
"""


def func(matrix):
    length = len(matrix)
    # 对角翻转
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 水平翻转
    for i in range(length):
        for j in range(length // 2):
            matrix[i][j], matrix[i][length - 1 - j] = matrix[i][length - 1 - j], matrix[i][j]


if __name__ == "__main__":
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    func(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()
    # print(matrix)
