"""
Accepted
"""


def func(haystack, needle):
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


if __name__ == "__main__":
    haystack = "aaaaa"
    needle = "bba"
    print(func(haystack, needle))
