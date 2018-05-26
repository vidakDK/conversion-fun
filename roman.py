import re
import time
from collections import OrderedDict


class IterativeConversion:

    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
               (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def num2roman(self, num):
        roman = ''
        while num > 0:
            for i, r in self.num_map:
                while num >= i:
                    roman += r
                    num -= i
        return roman


class RegexConversion:
    #Define exceptions
    # class RomanError(Exception):
    #     pass
    # class OutOfRangeError(RomanError):
    #     pass
    # class NotIntegerError(RomanError):
    #     pass
    # class InvalidRomanNumeralError(RomanError):
    #     pass

    #Define digit mapping
    romanNumeralMap = (('M',  1000),
                       ('CM', 900),
                       ('D',  500),
                       ('CD', 400),
                       ('C',  100),
                       ('XC', 90),
                       ('L',  50),
                       ('XL', 40),
                       ('X',  10),
                       ('IX', 9),
                       ('V',  5),
                       ('IV', 4),
                       ('I',  1))

    def toRoman(self, n):
        """convert integer to Roman numeral"""
        # if not (0 < n < 5000):
        #     raise RegexConversion.OutOfRangeError("number out of range (must be 1..4999)")
        # if int(n) != n:
        #     raise RegexConversion.NotIntegerError("decimals can not be converted")

        result = ""
        for numeral, integer in self.romanNumeralMap:
            while n >= integer:
                result += numeral
                n -= integer
        return result

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


class RecursiveConversion:
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def write_roman(self, num):
        def roman_num(num, roman):
            for r in roman.keys():
                x, y = divmod(num, r)
                yield roman[r] * x
                num -= (r * x)
                if num > 0:
                    roman_num(num, roman)
                else:
                    break

        return "".join([a for a in roman_num(num, self.roman)])


def test_ic(n):
    c = IterativeConversion()
    for i in range(n):
        c.num2roman(i)


def test_regc(n):
    c = RegexConversion()
    for i in range(n):
        c.toRoman(i)


def test_recc(n):
    c = RecursiveConversion()
    for i in range(n):
        c.write_roman(i)


if __name__ == '__main__':
    import timeit

    print("Iterative: {}".format(timeit.timeit("test_ic(5000)", setup="from __main__ import test_ic", number=1000)))
    print("Regex: {}".format(timeit.timeit("test_regc(5000)", setup="from __main__ import test_regc", number=1000)))
    print("Recursive: {}".format(timeit.timeit("test_recc(5000)", setup="from __main__ import test_recc", number=1000)))
