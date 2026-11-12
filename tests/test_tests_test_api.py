"""Smoke tests for tests_test_api."""
import unittest

from finance_quant_api import tests_test_api


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(tests_test_api, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(tests_test_api) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
