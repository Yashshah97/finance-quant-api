import unittest
from finance_quant_api import utils_validation

class TestUtilsValidation(unittest.TestCase):

    def test_is_positive_integer(self):
        self.assertTrue(utils_validation.is_positive_integer(5))
        self.assertFalse(utils_validation.is_positive_integer(-1))
        self.assertFalse(utils_validation.is_positive_integer(0))

    def test_is_non_negative_integer(self):
        self.assertTrue(utils_validation.is_non_negative_integer(5))
        self.assertTrue(utils_validation.is_non_negative_integer(0))
        self.assertFalse(utils_validation.is_non_negative_integer(-1))

    def test_validate_positive_integer(self):
        utils_validation.validate_positive_integer("test", 5)
        with self.assertRaises(ValueError):
            utils_validation.validate_positive_integer("test", -1)

    def test_validate_non_negative_integer(self):
        utils_validation.validate_non_negative_integer("test", 5)
        utils_validation.validate_non_negative_integer("test", 0)
        with self.assertRaises(ValueError):
            utils_validation.validate_non_negative_integer("test", -1)

    def test_validate_string(self):
        utils_validation.validate_string("test", "hello")
        with self.assertRaises(ValueError):
            utils_validation.validate_string("test", 123)

    def test_validate_list(self):
        utils_validation.validate_list("test", [1, 2, 3])
        with self.assertRaises(ValueError):
            utils_validation.validate_list("test", "hello")

if __name__ == '__main__':
    unittest.main()
