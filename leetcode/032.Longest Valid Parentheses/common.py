"""
Accepted
利用堆栈

遍历字符串，
遇到“（”就将其索引压入堆栈中，遇到“）”则弹出栈顶元素
此时判断，堆栈是否为空，
如果为空，则把当前索引压入，
如果不为空，说明还有合法的需要继续遍历匹配，则将结果取出
"""


def func(s):
    result = 0
    tmp = []
    tmp.append(-1)
    for i in range(len(s)):
        if s[i] == "(":
            tmp.append(i)
        else:
            tmp.pop(-1)
            if len(tmp) == 0:
                tmp.append(i)
            else:
                result = max(result, i - tmp[-1])
    return result


if __name__ == "__main__":
    s = "(())()"
    print(func(s))
