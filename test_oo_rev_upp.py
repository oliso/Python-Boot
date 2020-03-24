"""

Script for testing oo_rev_upp.py .

Project: Python Boot Camp
Author: OO

"""

import pytest


def rev_upp(input_strings):
    """Input must be a single string or a list."""
    output = []

    # Check if list:
    if type(input_strings) == list:

        for s in input_strings:

            if type(s) == str:

                # Upper case:
                uppercased = s.upper()

                # Reverse:
                reversed = uppercased[::-1]

                output.append(reversed)

                if s == input_strings[-1]:
                    return output

            else:
                raise Exception("Input arg must be a list of strings!")

    # Check if string:
    elif type(input_strings) == str:

        # Upper case:
        uppercased = input_strings.upper()

        # Reverse:
        reversed = uppercased[::-1]

        output.append(reversed)

        return output

    else:
        raise Exception("Input arg must be a string!")


# Test a range of valid inputs:
def test_output_rev_upp():
    assert rev_upp('Oliver') == ['REVILO']
    assert rev_upp(['Hello', 'World']) == ['OLLEH', 'DLROW']
    assert rev_upp('#/,"') == ['",/#']


# Test invalid inputs:
def test_invalid_rev_upp():
    with pytest.raises(Exception):
        assert rev_upp(123)
        assert rev_upp(['Hello', 123])
