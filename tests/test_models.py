"""Smoke tests for models."""
import unittest

from finance_quant_api import models


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(models, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(models) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
