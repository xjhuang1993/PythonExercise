"""
Accepted
"""


def func(matrix, target):
    row = len(matrix)
    if not row:
        return False
    col = len(matrix[0])

    left = 0
    right = row * col - 1
    while left <= right:
        mid = (left + right) // 2
        num = matrix[mid // col][mid % col]
        if num == target:
            return True
        if num < target:
            left = mid + 1
        if num > target:
            right = mid - 1
    return False


if __name__ == "__main__":
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    print(func(matrix, target))
