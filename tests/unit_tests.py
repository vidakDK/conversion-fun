import unittest
from roman_conversion import roman2int, int2roman, InputError


class KnownValues(unittest.TestCase):
    known_values = ((1, 'I'),
                    (2, 'II'),
                    (3, 'III'),
                    (4, 'IV'),
                    (5, 'V'),
                    (6, 'VI'),
                    (7, 'VII'),
                    (8, 'VIII'),
                    (9, 'IX'),
                    (10, 'X'),
                    (50, 'L'),
                    (100, 'C'),
                    (500, 'D'),
                    (1000, 'M'),
                    (31, 'XXXI'),
                    (148, 'CXLVIII'),
                    (294, 'CCXCIV'),
                    (312, 'CCCXII'),
                    (421, 'CDXXI'),
                    (528, 'DXXVIII'),
                    (621, 'DCXXI'),
                    (782, 'DCCLXXXII'),
                    (870, 'DCCCLXX'),
                    (941, 'CMXLI'),
                    (1043, 'MXLIII'),
                    (1110, 'MCX'),
                    (1226, 'MCCXXVI'),
                    (1301, 'MCCCI'),
                    (1485, 'MCDLXXXV'),
                    (1509, 'MDIX'),
                    (1607, 'MDCVII'),
                    (1754, 'MDCCLIV'),
                    (1832, 'MDCCCXXXII'),
                    (1993, 'MCMXCIII'),
                    (2074, 'MMLXXIV'),
                    (2152, 'MMCLII'),
                    (2212, 'MMCCXII'),
                    (2343, 'MMCCCXLIII'),
                    (2499, 'MMCDXCIX'),
                    (2574, 'MMDLXXIV'),
                    (2646, 'MMDCXLVI'),
                    (2723, 'MMDCCXXIII'),
                    (2892, 'MMDCCCXCII'),
                    (2975, 'MMCMLXXV'),
                    (3051, 'MMMLI'),
                    (3185, 'MMMCLXXXV'),
                    (3250, 'MMMCCL'),
                    (3313, 'MMMCCCXIII'),
                    (3408, 'MMMCDVIII'),
                    (3501, 'MMMDI'),
                    (3610, 'MMMDCX'),
                    (3743, 'MMMDCCXLIII'),
                    (3844, 'MMMDCCCXLIV'),
                    (3888, 'MMMDCCCLXXXVIII'),
                    (3940, 'MMMCMXL'),
                    (3999, 'MMMCMXCIX'))

    def test_int2roman_known(self):
        """Integer to Roman correctness for known values."""
        for integer, numeral in self.known_values:
            result = int2roman(integer)
            self.assertEqual(numeral, result)

    def test_roman2int_known(self):
        """ROman to Integer correctness for known values."""
        for integer, numeral in self.known_values:
            result = roman2int(numeral)
            self.assertEqual(integer, result)


class TestStringInput(unittest.TestCase):
    def test_int2roman(self):
        """Test if string input works correctly."""
        input_str = "55"
        result = int2roman(input_str)
        self.assertEqual(result, "LV")


class TestBadInput(unittest.TestCase):
    def test_roman2int(self):
        """Test if error raising works for bad input string."""
        for s in ['MMMMM', 'DD', 'CCCC', "", "VIV", "XLXL", "vi"]:
            self.assertRaises(InputError, roman2int, s)

    def test_int2roman(self):
        """Test if error raising works for bad input integer."""
        for num in [0, -1, 1.5, "V", "", [1,2], [], 5000]:
            self.assertRaises(InputError, int2roman, num)


class TestBackForth(unittest.TestCase):
    def test_back_forth(self):
        """Test if conversion int2roman and roman2int gives same results."""
        for num in range(1, 5000):
            self.assertEqual(num, roman2int(int2roman(num)))


if __name__ == '__main__':
    unittest.main()

    import roman
