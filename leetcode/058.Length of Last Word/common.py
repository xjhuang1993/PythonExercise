"""
Accepted
"""


def func(s):
    if not s:
        return 0
    result_list = s.strip().split(" ")
    result = len(result_list[-1])
    return result


if __name__ == "__main__":
    s = "Hello World"
    print(func(s))
