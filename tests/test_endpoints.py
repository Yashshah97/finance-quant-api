import unittest
from http import HTTPStatus
from finance_quant_api import endpoints

class TestEndpoints(unittest.TestCase):

    def test_get_time_series_valid_request(self):
        request = {'symbol': 'AAPL'}
        response, status_code = endpoints.get_time_series(request)
        self.assertEqual(status_code, HTTPStatus.OK)

    def test_get_time_series_invalid_symbol(self):
        request = {}
        response, status_code = endpoints.get_time_series(request)
        self.assertEqual(status_code, HTTPStatus.BAD_REQUEST)

    def test_get_risk_metrics_valid_request(self):
        request = {'symbol': 'AAPL'}
        response, status_code = endpoints.get_risk_metrics(request)
        self.assertEqual(status_code, HTTPStatus.OK)

    def test_get_risk_metrics_invalid_symbol(self):
        request = {}
        response, status_code = endpoints.get_risk_metrics(request)
        self.assertEqual(status_code, HTTPStatus.BAD_REQUEST)

if __name__ == '__main__':
    unittest.main()
