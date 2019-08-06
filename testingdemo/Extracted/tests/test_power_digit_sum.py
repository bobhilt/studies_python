import unittest
import power_digit_sum2 as pds

class PowerDigitSum(unittest.TestCase):

    def test_digits_of_2_to_15th_is_26(self):
        self.assertEqual(pds.power_digit_sum(15),26)

    def test_sum_of_digits_of_2_to_10th_is_7(self):
        self.assertEqual(pds.power_digit_sum(10),7)

    # def test_negative_power_raises_value_error(self):
    #     with self.assertRaises(ValueError):
    #         x =pds.power_digit_sum(-10)
