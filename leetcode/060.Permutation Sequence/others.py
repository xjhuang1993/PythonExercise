"""
Accepted
"""


def func(n, k):
    nums = [x for x in range(1, n + 1)]
    result = ''
    k -= 1
    while n > 0:
        n -= 1
        # get the index of current digit
        factorial = 1
        for i in range(n):
            factorial *= i + 1
        index, k = divmod(k, factorial)
        result += str(nums[index])
        # remove handled number
        nums.remove(nums[index])

    return result


if __name__ == "__main__":
    n = 3
    k = 2
    print(func(n, k))
