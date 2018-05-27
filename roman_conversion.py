"""Roman/Integer conversion module"""

import re

# We use two versions of Roman Numeral mappings, extended and basic, to maximize algorithm efficiency.
__extended_map = [('M', 1000),
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

__bmap = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}  # basic map - used for optimization


# Regex pattern to validate the input Roman numeral string (values 1-4999).
__roman_numeral_regex = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """, re.VERBOSE)


def int2roman(num):
    """Integer to Roman coversion.

    Uses the extended Roman numeral map to go through the integer value and
    substract the values of Roman numerals iteratively.

    :param num: integer representation of the input number
    :return: string representation of the input number in Roman numerals
    """
    try:
        num_int = int(num)
    except ValueError:
        raise InputError(num, "Input value must be in integer representation.")
    except TypeError:
        raise InputError(num, "Input must be a number, string, or a bytes-like object.")
    if num != num_int:
        raise InputError(num, "Input cannot be a non-integer decimal value.")
    else:
        num = int(num)
    if not 0 < num < 5000:
        raise InputError(num, "Input must be an integer in [1,4999] range.")

    res = ""
    for r, i in __extended_map:
        while num >= i:
            res += r
            num -= i
    return res


def roman2int(s):
    """Roman to Integer conversion.

    Uses zip() to compare two versions of the string s, shifted by one, and compares the elements, deciding whether
    to add or subtract the value from the total sum.

    Example:
        s = "MDIX" should be converted to 1509
        Iterating through zip() gives us:
        M D -> +1000
        D I -> +500
        I X -> -1
        which is 1499 in total.
        Finally we add the s[-1] term, which is X -> 10:

            result = 1499 + 10 = 1509.

    :param s: string representation of the Roman number in the integer range of 1-4999.
    :return: integer representation of the input number.
    """
    if not s or not isinstance(s, str):
        raise InputError(s, "Input value must be a non-empty string.")
    elif __roman_numeral_regex.search(s) is None:
        raise InputError(s, "Input is not a valid Roman numeral representation of numbers in the 1-4999 range.")

    return sum([__bmap[i] if __bmap[i] >= __bmap[j] else -__bmap[i] for i, j in zip(s, s[1:])]) + __bmap[s[-1]]


class Error(Exception):
    """Base class for exceptions in conversion between Roman and Integer number representations."""
    pass


class InputError(Error):
    """Exception raised for errors in the input number.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
