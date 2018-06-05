"""
Accepted
采用堆栈（后进先出）进行配对
"""


def func(s):
    stack = []
    d = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for ch in s:
        if ch in d.values():
            stack.append(ch)
        elif ch in d.keys():
            if stack == [] or d[ch] != stack.pop():
                return False
        else:
            return False
    return stack == []


if __name__ == "__main__":
    s = "(])"
    print(func(s))
