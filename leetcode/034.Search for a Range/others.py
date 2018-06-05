"""
Accepted
二分法
Time complexity : O(lgn)
没懂
"""


def func(nums, target):
    left_idx = sub_func(nums, target, True)

    # assert that `left_idx` is within the array bounds and that `target`
    # is actually in `nums`.
    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]

    return [left_idx, sub_func(nums, target, False) - 1]


def sub_func(nums, target, left):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target or (left and target == nums[mid]):
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    nums = [1]
    target = 0
    print(func(nums, target))
