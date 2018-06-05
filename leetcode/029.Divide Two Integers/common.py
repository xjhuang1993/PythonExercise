"""
Time Limit Exceeded
乘法本质是加法，除法本质是减法，减法本质是加法
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
        abs_dividend -= abs_divisor
        result += 1
    return result if sign else -result


if __name__ == "__main__":
    dividend = 1
    divisor = -1
    print(func(dividend, divisor))
