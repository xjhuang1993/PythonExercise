
def func(s, p):
    if not p:
        return not s
    first_match = bool(s) and p[0] in [s[0], '.']
    if len(p) > 1 and p[1] == '*':
        return func(s, p[2:]) or first_match and func(s[1:], p)
    else:
        return first_match and func(s[1:], p[1:])


if __name__ == "__main__":
    s = "aa"
    p = "a"
    print(func(s, p))
