"""
Accepted
"""


def func(sl):
    sl = sorted(sl)
    length = len(sl)
    if length == 0:
        return ""
    result = sl[0]
    for i in range(len(result)):
        tmp = result[i]
        for j in range(1, len(sl)):
            if sl[j][i] != tmp or i == len(sl[j]):
                return result[:i]
    return result


if __name__ == "__main__":
    sl = ["aa", "ab", "a"]
    print(func(sl))
