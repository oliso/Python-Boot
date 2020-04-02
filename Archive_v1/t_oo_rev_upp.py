"""

Script for testing oo_rev_upp.py .

Project: Python Boot Camp
Author: OO

"""

import pytest
import oo_rev_upp as ru


# Test a range of valid inputs:
def test_output_rev_upp():
    assert ru.rev_upp('Oliver') == ['REVILO']
    assert ru.rev_upp(['Hello', 'World']) == ['OLLEH', 'DLROW']
    assert ru.rev_upp('#/,"') == ['",/#']


# Test invalid inputs:
def test_invalid_rev_upp():
    with pytest.raises(Exception):
        assert ru.rev_upp(123)
        assert ru.rev_upp(['Hello', 123])
