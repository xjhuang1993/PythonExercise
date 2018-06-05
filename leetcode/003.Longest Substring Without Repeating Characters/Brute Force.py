"""
Time Limit Exceeded
Time complexity : O(n^3).
Space complexity : O(min(n, m)).
"""


def func(s):

    def all_unique(s):
        tmpset = set()
        for i in range(len(s)):
            if s[i] not in tmpset:
                tmpset.add(s[i])
                continue
            return False
        return True

    result = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if all_unique(s[i:j]):
                result = max(result, j - i)
            else:
                break
    return result


if __name__ == "__main__":
    s = ""
    print(func(s))

