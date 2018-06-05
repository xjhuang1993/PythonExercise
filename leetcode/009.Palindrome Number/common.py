"""

"""


def func(x: int):
    s = str(x)
    if len(s) == 1:
        return True
    n = len(s) - 1
    m = 0
    while m <= n:
        if s[m] == s[n]:
            m = m + 1
            n = n - 1
        else:
            break
    else:
        return True
    return False


if __name__ == "__main__":
    x = 121
    print(func(x))
