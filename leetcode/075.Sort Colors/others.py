"""
Accepted
two-pass algorithm using counting sort
"""


def func(nums):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1
    for i in range(count_0):
        nums[i] = 0
    for i in range(count_0, count_0 + count_1):
        nums[i] = 1
    for i in range(count_0 + count_1, len(nums)):
        nums[i] = 2


if __name__ == "__main__":
    nums = [0, 2, 1, 1, 2, 0, 0, 1]
    func(nums)
    print(nums)
