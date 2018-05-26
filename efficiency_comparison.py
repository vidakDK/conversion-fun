"""Comparison of different algorithms for Roman<->Integer conversion"""

__author__ = "Vidak Kazic (vidak.kazic@gmail.com)"
__date__ = "26/05/2018"


"""
This module compares three different Integer to Roman algorithms and three different Roman to Integer algorithms,
and does a timing analysis to find the fastest algorithm, since we are not concerened with memory for this type
of problem.
"""
import timeit

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

l = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def num2roman_iter(num):
    """Integer to Roman algorithm based on classic addition/subtraction."""
    res = ""
    for r, i in roman_numeral_map:
        while num >= i:
            res += r
            num -= i
    return res


def num2roman_divmod(num):
    """Integer to Roman algorithm based on divmod function."""
    res = ""
    for r, i in roman_numeral_map:
        factor, num = divmod(num, i)
        res += r * factor
        if num == 0:
            break
    return res


def num2roman_string(num):
    """Integer to Roman algorithm based on string replace.
    It starts from a string of I characters that it then replaces by priority."""
    res = "I"*num
    return res \
        .replace("IIIII", "V") \
        .replace("IIII", "IV") \
        .replace("VV", "X") \
        .replace("VIV", "IX") \
        .replace("XXXXX", "L") \
        .replace("XXXX", "XL") \
        .replace("LL", "C") \
        .replace("LXL", "XC") \
        .replace("CCCCC", "D") \
        .replace("CCCC", "CD") \
        .replace("DD", "M") \
        .replace("DCD", "CM")


def roman2num_bigmap(s):
    """Roman to Integer algorithm based on full numeral mapping."""
    res = 0
    index = 0
    for r, i in roman_numeral_map:
        while s[index:index+len(r)] == r:
            res += i
            index += len(r)
    return res


def roman2num_iter(s):
    """Roman to Integer algorithm based on classic subtraction and reduced numeral mapping."""
    result = 0
    for i in range(len(s)):
        result += l[s[i]]
        if i > 0 and l[s[i - 1]] < l[s[i]]:
            result -= l[s[i - 1]] * 2
    return result


def roman2num_iter2(s):
    """Roman to Integer algorithm based on subtraction and Python zip function for efficiency,
    with reduced numeral mapping."""
    return sum([l[i] if l[i] >= l[j] else -l[i] for i, j in zip(s, s[1:])]) + l[s[-1]]


def algorithm_timer(fun, test_set, num_iterations):
    """
    Time specific algorithm for the Integer to Roman conversion.

    :param fun: function object
    :param test_set: set of values to convert
    :param num_iterations: timeit number of iterations
    """
    return("Algorithm: {}\nDescription: {}\nExecution time: {} seconds.\n***********".format(
        fun.__name__,
        fun.__doc__,
        timeit.timeit(
            "for i in {}: {}(i)".format(test_set, fun.__name__),
            setup="from __main__ import {}".format(fun.__name__),
            number=num_iterations
        )
    ))


if __name__ == '__main__':
    # Test Roman to Integer algorithms:
    test_set = ['I', 'IV', 'XIX', 'LIV', 'DCCLXXII', 'MCCCXXIV', 'MMMMCMXCIX']
    print("\n\n")
    print(algorithm_timer(roman2num_iter, test_set, 10000))
    print(algorithm_timer(roman2num_iter2, test_set, 10000))
    print(algorithm_timer(roman2num_bigmap, test_set, 10000))

    # Test Integer to Roman algorithms:
    test_set = list(range(5000))
    print("\n\n")
    print(algorithm_timer(num2roman_iter, test_set, 100))
    print(algorithm_timer(num2roman_divmod, test_set, 100))
    print(algorithm_timer(num2roman_string, test_set, 100))
