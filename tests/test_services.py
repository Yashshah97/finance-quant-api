"""Smoke tests for services."""
import unittest

from finance_quant_api import services


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(services, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(services) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
