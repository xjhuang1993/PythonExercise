"""
Accepted
这道题需要读懂题目，nums[i]的值是能跳到的最大跨度，而不是下一跳所在的index
也就是说应该检查0<i<nums[i]的所有i
以此遍历
"""


def func(nums):
    length = len(nums)
    next_index = index = 0
    while index < length and index <= next_index:
        next_index = max(index + nums[index], next_index)
        index += 1
    return index == length


if __name__ == "__main__":
    nums = [0, 1]
    print(func(nums))
