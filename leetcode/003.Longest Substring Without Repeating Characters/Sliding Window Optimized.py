"""
Accepted
Time complexity : O(n).
Space complexity : O(min(m, n)).
"""


def func(s):
    result = 0
    tmpdict = dict()
    tmp = 0
    for i in range(len(s)):
        if s[i] in tmpdict:
            tmp = max(tmp, tmpdict[s[i]])
        result = max(result, i - tmp + 1)
        tmpdict[s[i]] = i + 1
    return result


if __name__ == "__main__":
    s = "abcacbb"
    print(func(s))
