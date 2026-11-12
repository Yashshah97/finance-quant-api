import unittest
from finance_quant_api import tests_test_api

class TestTestAPI(unittest.TestCase):

    def test_empty_request(self):
        with self.assertRaises(ValueError):
            tests_test_api.TestAPI().test_empty_request()

    def test_invalid_method(self):
        from unittest.mock import patch, Mock
        with patch('finance_quant_api.api.app.request_handler') as mock_handler:
            mock_handler.return_value = None
            tests_test_api.TestAPI().test_invalid_method()
            mock_handler.assert_called_once_with('GET', {'method': 'invalid'})

    def test_empty_body(self):
        response = tests_test_api.TestAPI().test_empty_body()
        self.assertEqual(response.status_code, 400)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            tests_test_api.TestAPI().test_invalid_input()

    def test_valid_request(self):
        response = tests_test_api.TestAPI().test_valid_request()
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
