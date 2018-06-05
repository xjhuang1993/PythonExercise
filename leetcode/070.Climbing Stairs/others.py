"""
Accepted
仔细观察这个问题，其实解出来的列表是一个斐波那契数列
所以解题就变成了斐波那契数列第n个数
"""


def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    n1 = 1
    n2 = 2
    for i in range(2, n):
        n1, n2 = n2, n1 + n2
    return n2


if __name__ == "__main__":
    n = 5
    print(func(n))
