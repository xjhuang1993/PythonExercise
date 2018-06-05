"""
Time Limit Exceeded
"""


def func(nums):
    sums = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sums.append(sum(nums[i:j + 1]))
    return max(sums)


if __name__ == "__main__":
    nums = [1]
    print(func(nums))
