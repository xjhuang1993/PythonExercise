"""
Accepted
"""


def func(nums):
    result = list()
    nums.sort()
    length = len(nums)
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = length - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < 0:
                j = j + 1
            elif s > 0:
                k = k - 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                while j + 1 < length and nums[j] == nums[j + 1]:
                    j = j + 1
                while k + 1 < length and [k] == nums[k - 1]:
                    k = k - 1
                j = j + 1
                k = k - 1
    return result


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(func(nums))  # [[-1,-1,2],[-1,0,1]]
