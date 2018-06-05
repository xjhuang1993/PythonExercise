"""
Accepted
"""


def func(nums, target):
    if not nums:
        return 0
    try:
        return nums.index(target)
    except ValueError:
        try:
            for i in range(len(nums)):
                if nums[i + 1] > target > nums[i]:
                    return i + 1
        except IndexError:
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 7
    print(func(nums, target))
