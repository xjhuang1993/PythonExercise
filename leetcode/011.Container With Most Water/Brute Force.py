"""
Time Limit Exceeded
"""


def func(height):
    result = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            result = max(result, min(height[i], height[j]) * (j - i))
    return result


if __name__ == "__main__":
    height = [1, 1]
    print(func(height))
