"""
Accepted
one-pass algorithm using counting sort
"""


def func(nums):
    index_0 = 0
    index_1 = 0
    for i in range(len(nums)):
        tmp = nums[i]
        nums[i] = 2
        if tmp < 2:
            nums[index_1] = 1
            index_1 += 1
        if tmp == 0:
            nums[index_0] = 0
            index_0 += 1


if __name__ == "__main__":
    nums = [0, 2, 1, 1, 2, 0, 0, 1]
    func(nums)
    print(nums)
