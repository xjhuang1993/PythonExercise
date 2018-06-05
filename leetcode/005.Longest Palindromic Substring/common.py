"""
Accepted
Time complexity : O(n^2).
Space complexity : O(1).
"""


def func(s):
    m = 0
    result = s
    length = len(s)
    for i in range(length):
        left = i
        right = i
        while right < length and s[i] == s[right]:
            right = right + 1
        while left - 1 >= 0 and right < length and s[left - 1] == s[right]:
            left = left - 1
            right = right + 1
        if m < right - left:
            m = right - left
            result = s[left:right]
    return result


if __name__ == "__main__":
    s = "aaa"
    print(func(s))
