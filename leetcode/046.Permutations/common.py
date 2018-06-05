"""
Accepted
前面好些题都是深度优先搜索DFS
"""


def func(nums):
    result = []
    dfs(nums, [], result)
    return result


def dfs(nums, path, result):
    if not nums:
        result.append(path)
        return
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], result)


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(func(nums))
