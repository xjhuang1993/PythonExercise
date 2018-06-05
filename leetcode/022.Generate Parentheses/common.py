"""
Accepted
注意递归的方式以及结束的标志
"""


def func(n):
    l = list()
    sub_func(l, "", 0, 0, n)
    return l


def sub_func(l, s, left, right, n):
    if len(s) == n * 2:
        l.append(s)
        return
    if left < n:
        sub_func(l, s + "(", left + 1, right, n)
    if right < left:
        sub_func(l, s + ")", left, right + 1, n)


if __name__ == "__main__":
    n = 3
    print(func(n))
