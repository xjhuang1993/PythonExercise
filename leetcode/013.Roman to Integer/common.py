

def func(roman_num):
    romannum_to_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    i = 0
    while i < len(roman_num):
        if roman_num[i] == "I" and i + 1 < len(roman_num) and roman_num[i + 1] == "V":
            result = result + romannum_to_num["V"] - romannum_to_num["I"]
            i = i + 2
        elif roman_num[i] == "I" and i + 1 < len(roman_num) and roman_num[i + 1] == "X":
            result = result + romannum_to_num["X"] - romannum_to_num["I"]
            i = i + 2
        elif roman_num[i] == "X" and i + 1 < len(roman_num) and roman_num[i + 1] == "L":
            result = result + romannum_to_num["L"] - romannum_to_num["X"]
            i = i + 2
        elif roman_num[i] == "X" and i + 1 < len(roman_num) and roman_num[i + 1] == "C":
            result = result + romannum_to_num["C"] - romannum_to_num["X"]
            i = i + 2
        elif roman_num[i] == "X" and i + 1 < len(roman_num) and roman_num[i + 1] == "D":
            result = result + romannum_to_num["D"] - romannum_to_num["X"]
            i = i + 2
        elif roman_num[i] == "C" and i + 1 < len(roman_num) and roman_num[i + 1] == "M":
            result = result + romannum_to_num["M"] - romannum_to_num["C"]
            i = i + 2
        else:
            result = result + romannum_to_num[roman_num[i]]
            i = i + 1
    return result


if __name__ == "__main__":
    roman_num = "X"
    print(func(roman_num))
