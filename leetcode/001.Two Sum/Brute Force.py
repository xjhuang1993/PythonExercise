"""
Accepted
Time complexity : O(n^2). Space complexity : O(1).
"""


def func(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    raise ValueError("No two sum solution")


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(func(nums, target))
