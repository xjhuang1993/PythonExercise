"""
Accepted
没懂
"""


def func(nums):
    if not nums:
        return 0
    cur_sum = max_sum = nums[0]
    for num in nums[1:]:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)
    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(func(nums))
