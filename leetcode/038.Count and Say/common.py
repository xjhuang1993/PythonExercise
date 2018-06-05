"""
Accepted
关键是读懂题目
当n=1时，输出1
当n=2时，数上一个字符串中的数值个数，上一个字符串中有1个1，所以输出11
当n=3时，数上一个字符串中的数值个数，上一个字符串中有2个1，所以输出21
当n=4时，数上一个字符串中的数值个数，上一个字符串中有1个2、1个1，所以输出1211
......
当n=n时...
"""


def func(n):
    if n == 1:
        return "1"
    pre_s = func(n - 1) + '*'  # 添加一个无关的*，防止指针溢出
    count = 1
    result = ""
    for i in range(len(pre_s) - 1):
        if pre_s[i] == pre_s[i + 1]:
            count += 1
        else:
            result = result + str(count) + pre_s[i]
            count = 1
    return result


if __name__ == "__main__":
    n = 5
    print(func(n))
