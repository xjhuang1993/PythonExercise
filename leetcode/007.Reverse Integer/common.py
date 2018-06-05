"""

"""


def func(x):
    sign = (x > 0) - (x < 0)
    result = int(str(x * sign)[::-1])
    return sign * result * (result < 2**31)


if __name__ == "__main__":
    x = -120
    print(func(x))
