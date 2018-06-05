"""
Accepted
"""


def func(nums, target):
    nums.sort()
    result = []
    dfs(nums, target, 0, [], result)
    return result


def dfs(nums, target, index, path, result):
    if target < 0:
        return
    if target == 0:
        result.append(path)
        return
    for i in range(index, len(nums)):
        dfs(nums, target - nums[i], i, path + [nums[i]], result)


if __name__ == "__main__":
    nums = [2, 3, 6, 7]
    target = 7
    print(func(nums, target))
