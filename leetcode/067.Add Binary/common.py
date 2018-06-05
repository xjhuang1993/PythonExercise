"""

"""


def func(a, b):
    if not a:
        return b
    if not b:
        return a
    a_2 = int(a, 2)
    b_2 = int(b, 2)
    result = a_2 + b_2
    return bin(result)[2:]


if __name__ == "__main__":
    a = "1"
    b = "1"
    print(func(a, b))
