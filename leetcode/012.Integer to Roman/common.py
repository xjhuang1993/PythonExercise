

def func(num):
    roman_num = {
        "M": ["", "M", "MM", "MMM"],
        "C": ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        "X": ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        "I": ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    }
    return roman_num["M"][num // 1000] + roman_num["C"][num % 1000 // 100] \
           + roman_num["X"][num % 100 // 10] + roman_num["I"][num % 10]


if __name__ == "__main__":
    num = 1
    print(func(num))
