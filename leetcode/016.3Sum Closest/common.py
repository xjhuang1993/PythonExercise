"""
Accepted
"""


def func(nums, target):
    result = nums[0] + nums[1] + nums[2]
    nums.sort()
    length = len(nums)
    for i in range(length - 2):
        j = i + 1
        k = length - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if abs(target - s) < abs(target - result):
                result = s
            if s > target:
                k = k - 1
            elif s < target:
                j = j + 1
            else:
                return s
    return result


if __name__ == "__main__":
    nums = [1, 1, 1, 0]
    target = -100
    print(func(nums, target))
