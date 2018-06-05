"""
Time Limit Exceeded
"""


def func(x):
    result = 0
    while True:
        if result * result <= x < (result + 1) * (result + 1):
            return result
        else:
            result += 1


if __name__ == "__main__":
    x = 4
    print(func(x))
