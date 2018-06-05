"""
Accepted
按照数学原理写出指数求解过程即可
"""


def func(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return func(1 / x, -n)
    elif n % 2:
        return x * func(x, n - 1)
    else:
        return func(x * x, n // 2)


if __name__ == "__main__":
    x = 2
    n = 10
    print(func(x, n))
