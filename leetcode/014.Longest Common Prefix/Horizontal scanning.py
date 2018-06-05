"""
Accepted
"""


def func(sl):
    length = len(sl)
    if length == 0:
        return ""
    result = sl[0]
    for i in range(1, length):
        while not sl[i].startswith(result):
            result = result[:-1]
            if len(result) == 0:
                return ""
    return result


if __name__ == "__main__":
    sl = ["aa"]
    print(func(sl))
