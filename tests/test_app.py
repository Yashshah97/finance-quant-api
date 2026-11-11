import unittest
from http import HTTPStatus
from unittest.mock import patch, MagicMock
from finance_quant_api import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('json.loads')
    def test_validate_input_json_decode_error(self, mock_json_loads):
        mock_json_loads.side_effect = json.JSONDecodeError('test', 'test', 0)
        response = self.app.post('/api/timeseries', data='invalid json')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_validate_input_valid_json(self):
        response = self.app.post('/api/timeseries', data='{"key": "value"}')
        self.assertEqual(response.status_code, HTTPStatus.OK)

if __name__ == '__main__':
    unittest.main()
