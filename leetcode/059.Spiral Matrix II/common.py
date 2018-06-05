"""
Accepted
直接模拟螺旋过程
"""


def func(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    row_begin = 0
    row_end = n - 1
    col_begin = 0
    col_end = n - 1
    num = 1
    while row_begin <= row_end and col_begin <= col_end:
        # 从左到右
        for j in range(col_begin, col_end + 1):
            matrix[row_begin][j] = num
            num += 1
        row_begin += 1
        # 从上到下
        for i in range(row_begin, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1
        # 从右到左
        if row_begin <= row_end:
            for j in range(col_end, col_begin - 1, -1):
                matrix[row_end][j] = num
                num += 1
        row_end -= 1
        # 从下到上
        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                matrix[i][col_begin] = num
                num += 1
        col_begin += 1

    return matrix


if __name__ == "__main__":
    n = 0
    print(func(n))
