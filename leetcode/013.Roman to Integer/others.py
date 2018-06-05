

def func(roman_num: str):
    result = 0
    if roman_num.find("IV") != -1:
        result = result - 2
    if roman_num.find("IX") != -1:
        result = result - 2
    if roman_num.find("XL") != -1:
        result = result - 20
    if roman_num.find("XC") != -1:
        result = result - 20
    if roman_num.find("CD") != -1:
        result = result - 200
    if roman_num.find("CM") != -1:
        result = result - 200
    for i in range(len(roman_num)):
        if roman_num[i] == "I":
            result = result + 1
        if roman_num[i] == "V":
            result = result + 5
        if roman_num[i] == "X":
            result = result + 10
        if roman_num[i] == "L":
            result = result + 50
        if roman_num[i] == "C":
            result = result + 100
        if roman_num[i] == "D":
            result = result + 500
        if roman_num[i] == "M":
            result = result + 1000
    return result


if __name__ == "__main__":
    roman_num = "X"
    print(func(roman_num))
