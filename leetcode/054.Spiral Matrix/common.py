"""
Accepted
直接模拟螺旋过程
"""


def func(matrix):
    result = []
    if not matrix:
        return result
    len_row = len(matrix)
    len_col = len(matrix[0])
    row_begin = 0
    row_end = len_row - 1
    col_begin = 0
    col_end = len_col - 1
    while row_begin <= row_end and col_begin <= col_end:
        # 从左到右
        for j in range(col_begin, col_end + 1):
            result.append(matrix[row_begin][j])
        row_begin += 1
        # 从上到下
        for i in range(row_begin, row_end + 1):
            result.append(matrix[i][col_end])
        col_end -= 1
        # 从右到左
        if row_begin <= row_end:
            for j in range(col_end, col_begin - 1, -1):
                result.append(matrix[row_end][j])
        row_end -= 1
        # 从下到上
        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                result.append(matrix[i][col_begin])
        col_begin += 1

    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3]
        # [4, 5, 6],
        # [7, 8, 9]
    ]
    print(func(matrix))
