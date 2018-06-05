"""
Accepted
直接搜索
Time complexity : O(n)O(n)
"""


def func(nums, target):
    length = len(nums)
    for i in range(length):
        if nums[i] == target:
            left = i
            break
    else:
        return [-1, -1]
    for i in range(length - 1, -1, -1):
        if nums[i] == target:
            right = i
            break
    return [left, right]


if __name__ == "__main__":
    nums = [2, 2, 2]
    target = 2
    print(func(nums, target))
