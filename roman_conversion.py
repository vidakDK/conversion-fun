import re
import time
from collections import OrderedDict

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


def num2roman_first(num):
    res = ""
    while num > 0:
        for r, i in roman_numeral_map:
            while num >= i:
                res += r
                num -= i
    return res

def num2roman_second(n):
    res = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            res += numeral
            n -= integer
    return res

#Define pattern to detect valid Roman numerals
romanNumeralPattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """ ,re.VERBOSE)

def fromRoman(self, s):
    """convert Roman numeral to integer"""
    # if not s:
    #     raise RegexConversion.InvalidRomanNumeralError("Input can not be blank")
    # if not RegexConversion.romanNumeralPattern.search(s):
    #     raise RegexConversion.InvalidRomanNumeralError("Invalid Roman numeral: {}".format(s))

    result = 0
    index = 0
    for numeral, integer in self.romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


if __name__ == '__main__':
    import timeit

    print("First version: {}".format(timeit.timeit("for i in range(5000): num2roman_first(i)", setup="from __main__ import num2roman_first", number=1000)))
    print("Second version: {}".format(timeit.timeit("for i in range(5000): num2roman_second(i)", setup="from __main__ import num2roman_second", number=1000)))
