"""
Accepted
通过减法和移位解决问题，左移移位其实就是乘以二，
把除数左移同时将被除数减去除数的值可以减少迭代次数。
"""


MAX_INT = 2147483647
MIN_INT = -2147483648


def func(dividend, divisor):
    if not divisor or dividend == MIN_INT and divisor == -1:
        return MAX_INT
    result = 0
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)
    sign = (dividend < 0) is (divisor < 0)
    while abs_dividend >= abs_divisor:
        tmp = abs_divisor
        i = 1
        while abs_dividend >= tmp:
            abs_dividend -= tmp
            result += i
            i <<= 1
            tmp <<= 1
    return result if sign else -result


if __name__ == "__main__":
    dividend = 15
    divisor = 3
    print(func(dividend, divisor))
