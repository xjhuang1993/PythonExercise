"""
Accepted
"""


def func(n, k):
    nums = [x + 1 for x in range(n)]
    result = []
    sub_func(nums, [], k, result)
    return result


def sub_func(nums, path, k, result):
    if len(path) == k:
        result.append(path)
        return
    for i in range(len(nums)):
        sub_func(nums[i + 1:], path + [nums[i]], k, result)


if __name__ == "__main__":
    n = 4
    k = 2
    print(func(n, k))
