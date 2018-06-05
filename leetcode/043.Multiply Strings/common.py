"""
Accepted
大数相乘，从低位到高位算，注意进位
"""


def func(num1, num2):
    result = [0] * (len(num1) + len(num2))
    for i, e1 in enumerate(reversed(num1)):
        for j, e2 in enumerate(reversed(num2)):
            result[i + j] += int(e1) * int(e2)
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return "".join(map(str, result[::-1]))


if __name__ == "__main__":
    num1 = "100"
    num2 = "100"
    print(func(num1, num2))
