"""
Accepted
与3sum对比，关键在于降维
"""


def func(nums, target):
    result = list()
    nums.sort()
    length = len(nums)
    for i in range(length - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, length - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j + 1
            l = length - 1
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                if s < target:
                    k = k + 1
                elif s > target:
                    l = l - 1
                else:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    while k + 1 < length and nums[k] == nums[k + 1]:
                        k = k + 1
                    while l + 1 < length and nums[l] == nums[l - 1]:
                        l = l - 1
                    k = k + 1
                    l = l - 1
    return result


if __name__ == "__main__":
    nums = [0, 0, 0, 0]
    target = 0
    print(func(nums, target))
