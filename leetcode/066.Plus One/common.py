"""
Accepted
"""


def func(digits):
    length = len(digits)
    for i in range(length - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits


if __name__ == "__main__":
    digits = [0]
    print(func(digits))
