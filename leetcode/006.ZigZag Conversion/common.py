"""
Time Limit Exceeded
按输出位置来对应输入位置
"""


def func(s, row):
    result = ""
    length = len(s)
    interval = row * 2 - 2
    for i in range(row):
        j = i
        while j < length:
            result = result + s[j]
            j = j + interval if i == 0 or i == row - 1 else j + interval - i * 2
    return result


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    row = 3
    print(func(s, row))





