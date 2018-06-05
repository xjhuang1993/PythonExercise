"""

"""


def func(s: str):
    int_max = 2147483647  # 2 ** 32 - 1
    int_min = -2147483648  # -2 ** 32
    s = s.strip()
    if len(s) == 0:
        return 0
    l = list(s)
    sign = -1 if l[0] == '-' else 1
    if l[0] in ['+', '-']:
        del l[0]
    index = 0
    result = 0
    while index < len(l) and l[index].isdigit():
        result = result * 10 + int(l[index])
        index = index + 1
    return max(int_min, min(sign * result, int_max))


if __name__ == "__main__":
    s = "-123"
    print(func(s))
