"""

Script for testing oo_rev_upp.py .

Project: Python Boot Camp
Author: OO

"""

import pytest
import oo_rev_upp_v2 as ru


# Test a range of valid inputs:
def test_output_rev_upp():
    assert ru.rev_upp(1, 'Oliver') == 'OLIVER'
    assert ru.rev_upp(2, 'Oliver') == 'revilO'
    assert ru.rev_upp(3, 'Oliver') == 'REVILO'
    assert ru.rev_upp(2, 'Hello World') == 'dlroW olleH'
    assert ru.rev_upp(3, '#/,"') == '",/#'


# Test invalid inputs:
def test_invalid_rev_upp():
    with pytest.raises(Exception):
        assert ru.rev_upp(123)
        assert ru.rev_upp(['Hello', 123])
        assert ru.rev_upp([1, 'Hello'])
        assert ru.rev_upp(3, 123)


# Test a range of valid inputs:
def test_output_rev():
    assert ru.rev('Oliver') == 'revilO'
    assert ru.rev('Hello World') == 'dlroW olleH'
    assert ru.rev('#/,"') == '",/#'


# Test invalid inputs:
def test_invalid_rev():
    with pytest.raises(Exception):
        assert ru.rev([1, 'Hello'])
        assert ru.rev(['Hello', 123])
        assert ru.rev(123)


# Test a range of valid inputs:
def test_output_upp():
    assert ru.upp('Oliver') == 'OLIVER'
    assert ru.upp('Hello World') == 'HELLO WORLD'
    assert ru.upp('#/,"') == '#/,"'


# Test invalid inputs:
def test_invalid_upp():
    with pytest.raises(Exception):
        assert ru.upp([1, 'Hello'])
        assert ru.upp(['Hello', 123])
        assert ru.upp(123)
