#! venv/bin/python3

import calculator2
import doctest
import unittest

def test_docs():
    doctest.testmod(calculator2)

class TestVatCalc(unittest.TestCase):
    def test_calculate_total(self):
        self.assertEqual(calculator2.calculate_total(200, 20), 240.0)


def test_vat_calc_calculate_total():
    assert calculator2.calculate_total(30, 15) == 34.5
    assert calculator2.calculate_total(75, 50) == 112.5


if __name__ == '__main__':
    test_docs()
    unittest.main()