#! venv/bin/python3

import calculator2
import doctest

def test_docs():
    doctest.testmod(calculator2)

if __name__ == '__main__':
    test_docs()