"""
Accepted
"""


def func(path):
    stack = []
    for p in path.split("/"):
        if p == "..":
            if stack:
                stack.pop()
        elif p and p != '.':
            stack.append(p)
    return "/" + "/".join(stack)


if __name__ == "__main__":
    path = "/a/."
    print(func(path))
