import unittest
from finance_quant_api import models

class TestDataModels(unittest.TestCase):

    def test_TimeSeries_init(self):
        data = {datetime.date(2022, 1, 1): 10.0, datetime.date(2022, 1, 2): 20.0}
        ts = models.TimeSeries('AAPL', data)
        self.assertEqual(ts.symbol, 'AAPL')
        self.assertEqual(ts.data, data)

    def test_TimeSeries_repr(self):
        data = {datetime.date(2022, 1, 1): 10.0, datetime.date(2022, 1, 2): 20.0}
        ts = models.TimeSeries('AAPL', data)
        self.assertEqual(repr(ts), "TimeSeries(symbol='AAPL', data={datetime.date(2022, 1, 1): 10.0, datetime.date(2022, 1, 2): 20.0})")

    def test_RiskMetrics_init(self):
        data = {'beta': 1.0, 'volatility': 2.0}
        rm = models.RiskMetrics('AAPL', data)
        self.assertEqual(rm.symbol, 'AAPL')
        self.assertEqual(rm.data, data)

    def test_RiskMetrics_repr(self):
        data = {'beta': 1.0, 'volatility': 2.0}
        rm = models.RiskMetrics('AAPL', data)
        self.assertEqual(repr(rm), "RiskMetrics(symbol='AAPL', data={'beta': 1.0, 'volatility': 2.0})")

    def test_Quote_init(self):
        q = models.Quote('AAPL', 10.0, 20.0)
        self.assertEqual(q.symbol, 'AAPL')
        self.assertEqual(q.bid, 10.0)
        self.assertEqual(q.ask, 20.0)

    def test_Quote_repr(self):
        q = models.Quote('AAPL', 10.0, 20.0)
        self.assertEqual(repr(q), "Quote(symbol='AAPL', bid=10.0, ask=20.0)")

if __name__ == '__main__':
    unittest.main()
