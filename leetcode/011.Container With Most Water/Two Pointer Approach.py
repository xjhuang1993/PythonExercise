"""
Accepted
"""


def func(height):
    result = 0
    left = 0
    right = len(height) - 1
    while left < right:
        result = max(result, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1
    return result


if __name__ == "__main__":
    height = [1, 1]
    print(func(height))
