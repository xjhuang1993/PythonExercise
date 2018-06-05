"""
Accepted
just count
"""


def func(nums):
    if not nums:
        return 0
    result = {}
    index = 0
    while index < len(nums):
        if nums[index] in result.keys():
            if result[nums[index]] == 2:
                nums.remove(nums[index])
                continue
            else:
                result[nums[index]] += 1
        else:
            result[nums[index]] = 1
        index += 1
    return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 1, 1]
    print(func(nums))
