"""
Accepted
"""


def func(digits):
    digit_to_letter = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    if len(digits) == 0:
        return []
    result = [""]
    for i in range(len(digits)):
        while len(result[0]) == i:
            tmp = result.pop(0)
            for s in digit_to_letter[digits[i]]:
                result.append(tmp + s)
    return result


if __name__ == "__main__":
    digits = "23"
    print(func(digits))
