"""
Accepted
伪暴力法
"""


def func(n):
    result = [0 for x in range(n + 1)]
    return sub_func(n, 0, result)


def sub_func(n, i, result):
    if i == n:
        return 1
    if i > n:
        return 0
    if result[i] > 0:
        return result[i]
    result[i] = sub_func(n, i + 1, result) + sub_func(n, i + 2, result)
    return result[i]


if __name__ == "__main__":
    n = 5
    print(func(n))
