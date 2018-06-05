"""
Accepted
"""


def func(nums):
    nums.sort()
    result = [[num] for num in nums]
    for num in nums:
        for r in result:
            if num > r[-1]:
                result.append(r + [num])
    result.append([])
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(func(nums))
