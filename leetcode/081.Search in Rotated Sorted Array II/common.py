"""
Accepted
莫名其妙
"""


def func(nums, target):
    try:
        if nums.index(target) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1
    print(func(nums, target))
