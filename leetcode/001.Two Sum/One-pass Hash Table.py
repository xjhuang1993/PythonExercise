"""
Accepted
Time complexity : O(n). Space complexity : O(n).
"""


def func(nums, target):
    tempdict = dict()
    for i in range(len(nums)):
        tempdiff = target - nums[i]
        if tempdiff in tempdict:
            return [tempdict[tempdiff], i]
        tempdict[nums[i]] = i
    raise ValueError("No two sum solution")


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(func(nums, target))
