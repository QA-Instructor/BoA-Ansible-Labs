#! venv/bin/python3

import calculator2
import doctest
import unittest
from unittest.mock import patch
import pytest


def test_docs():
    doctest.testmod(calculator2)

class TestVatCalc(unittest.TestCase):
    def test_calculate_total(self):
        self.assertEqual(calculator2.calculate_total(200, 20), 240.0)


def test_vat_calc_calculate_total():
    assert calculator2.calculate_total(30, 15) == 34.5
    assert calculator2.calculate_total(75, 50) == 112.5


def test_calc_input():
    with patch('calculator2.input') as inp:
        inp.return_value = "100@20"
        assert calculator2.calc_input_vat() == 120.0

def test_calc_input_with_50_20():
    with patch('calculator2.input') as inp:
        inp.return_value = "50@20"
        assert calculator2.calc_input_vat() == 60.0


def test_calc_inuit_vat_with_non_int_inputs():
    with pytest.raises(ValueError):
        with patch('calculator2.input') as inp:
            inp.return_value = "fifty@20"
            assert calculator2.calc_input_vat() == 60.0


if __name__ == '__main__':
    test_docs()
    unittest.main()