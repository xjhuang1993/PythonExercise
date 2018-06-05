"""
Time Limit Exceeded
"""


def is_palindrome(s):
    n = len(s) - 1
    m = 0
    while m <= n:
        if s[m] == s[n]:
            m = m + 1
            n = n - 1
        else:
            break
    else:
        return True
    return False


def func(s):
    max = 0
    result = s
    length = len(s)
    for i in range(length):
        for j in range(length, i, -1):
            if is_palindrome(s[i:j]) and j - i > max:
                max = j - i
                result = s[i:j]
                break
    return result


if __name__ == "__main__":
    s = "aaa"
    print(func(s))

