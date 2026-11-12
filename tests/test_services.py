import unittest
from finance_quant_api import services

class TestServices(unittest.TestCase):
    def test_calculate_mean(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(services.calculate_mean(data), 3)

    def test_calculate_volatility_empty_data(self):
        data = []
        with self.assertRaises(ValueError):
            services.calculate_volatility(data)

    def test_calculate_volatility_incomplete_data(self):
        data = [1, 2, 3]
        with self.assertRaises(ValueError):
            services.calculate_volatility(data)

    def test_validate_date_valid(self):
        date_str = "2022-01-01"
        self.assertTrue(services.validate_date(date_str))

    def test_validate_date_invalid(self):
        date_str = "20220101"
        self.assertFalse(services.validate_date(date_str))

    def test_validate_asset_valid(self):
        asset = "AAPL123"
        with self.assertRaises(ValueError):
            services.validate_asset(asset)

if __name__ == "__main__":
    unittest.main()
