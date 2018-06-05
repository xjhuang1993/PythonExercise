"""
Time Limit Exceeded
"""


def func(n, k):
    nums = [x + 1 for x in range(n)]
    result = []
    dfs(nums, [], result)
    return "".join(map(lambda x: str(x), result[k - 1]))


def dfs(nums, path, result):
    if not nums:
        result.append(path)
        return
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], result)


if __name__ == "__main__":
    n = 3
    k = 2
    print(func(n, k))
