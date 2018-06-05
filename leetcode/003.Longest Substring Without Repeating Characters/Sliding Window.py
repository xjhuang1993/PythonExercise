"""
Accepted
Time complexity : O(2n) = O(n)O(2n)=O(n).
Space complexity : O(min(m, n))O(min(m,n)).
"""


def func(s):
    n = len(s)
    result = 0
    i = 0
    j = 0
    tmpset = set()
    while i < n and j < n:
        if s[j] not in tmpset:
            tmpset.add(s[j])
            j = j + 1
            result = max(result, j - i)
        else:
            tmpset.remove(s[i])
            i = i + 1
    return result


if __name__ == "__main__":
    s = ""
    print(func(s))
