"""
Accepted
"""


def func(nums, val):
    if not nums:
        return 0
    n = nums.count(val)
    for i in range(n):
        nums.remove(val)
    return len(nums)


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    print(func(nums, val))
