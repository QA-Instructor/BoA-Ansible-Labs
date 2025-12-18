#! venv/bin/python3

import calculator2
import doctest
import unittest

def test_docs():
    doctest.testmod(calculator2)

class TestVatCalc(unittest.TestCase):
    def test_calculate_total(self):
        self.assertEqual(calculator2.calculate_total(200, 20), 240.0)

if __name__ == '__main__':
    test_docs()
    unittest.main()