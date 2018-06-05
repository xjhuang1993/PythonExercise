"""
Accepted
莫名其妙
"""


def func(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1


if __name__ == "__main__":
    nums = []
    target = 0
    print(func(nums, target))
