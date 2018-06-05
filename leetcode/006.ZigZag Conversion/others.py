"""
Accepted
按输入位置来对应输出位置
"""


def func(s, row):
    if row == 1:
        return s
    period = 2 * (row - 1)  # 第一行or最后一行字符间的对应输入串的位置差
    lines = ["" for i in range(row)]
    d = {j: j if j < row else (period - j) for j in range(period)}
    for k in range(len(s)):
        lines[d[k % period]] += s[k]
    return "".join(lines)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    row = 3
    print(func(s, row))
