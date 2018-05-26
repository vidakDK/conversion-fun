"""Comparison of different algorithms for Roman<->Integer conversion"""

__author__ = "Vidak Kazic (vidak.kazic@gmail.com)"
__date__ = "26/05/2018"

import re

# Number to Roman:
roman_numeral_map = [('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1)]


def num2roman_iter(num):
    """Algorithm based on classic addition/subtraction"""
    res = ""
    for r, i in roman_numeral_map:
        while num >= i:
            res += r
            num -= i
    return res


def num2roman_divmod(num):
    """Algorithm based on divmod function"""
    res = ""
    for r, i in roman_numeral_map:
        factor, num = divmod(num, i)
        res += r * factor
        if num == 0:
            break
    return res

def num2roman_string(num):
    """Algorithm based on string replace"""

    return "".join("I"*num))
    .replace("IIIII", "V")
    .replace("IIII", "IV")
    .replace("VV", "X")
    .replace("VIV", "IX")
    .replace("XXXXX", "L")
    .replace("XXXX", "XL")
    .replace("LL", "C")
    .replace("LXL", "XC")
    .replace("CCCCC", "D")
    .replace("CCCC", "CD")
    .replace("DD", "M")
    .replace("DCD", "CM");


def roman2num_regex(s):
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


l = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def roman2num_iter(s):
    result = 0
    for i in range(len(s)):
        result += l[s[i]]
        if i > 0 and l[s[i - 1]] < l[s[i]]:
            result -= l[s[i - 1]] * 2
    return result


def roman2num_iter2(s):
    return sum([l[i] if l[i] >= l[j] else -l[i] for i, j in zip(s, s[1:])]) + l[s[-1]]


if __name__ == '__main__':
    import timeit

    print("Integer to Roman timing test:")
    print("Iterative version: {}".format(timeit.timeit(
        "for i in range(5000): num2roman(i)",
        setup="from __main__ import num2roman", number=100
    )))

    print("Roman to Integer timing test:")
    values = ['I', 'IV', 'XIX', 'LIV', 'DCCLXXII', 'MCCCXXIV', 'MMMMCMXCIX']
    print("Iterative 1 version: {}".format(timeit.timeit(
        "for r in ['I', 'IV', 'XIX', 'LIV', 'DCCLXXII', 'MCCCXXIV', 'MMMMCMXCIX']: roman2num_iter(r)",
        setup="from __main__ import roman2num_iter", number=10000
    )))
    for v in values:
        print(roman2num_iter(v))

    print("Iterative 2 version: {}".format(timeit.timeit(
        "for r in ['I', 'IV', 'XIX', 'LIV', 'DCCLXXII', 'MCCCXXIV', 'MMMMCMXCIX']: roman2num_iter2(r)",
        setup="from __main__ import roman2num_iter2", number=10000
    )))
    for v in values:
        print(roman2num_iter2(v))

    print("Regex version: {}".format(timeit.timeit(
        "for r in ['I', 'IV', 'XIX', 'LIV', 'DCCLXXII', 'MCCCXXIV', 'MMMMCMXCIX']: roman2num_regex(r)",
        setup="from __main__ import roman2num_regex", number=10000
    )))
    for v in values:
        print(roman2num_regex(v))
