"""

Script for testing oo_rev_upp.py .

Project: Python Boot Camp
Author: OO

"""

import pytest
from oo_pbc_pkg import oo_rev_upp_v2 as ru


# Rev upp valid inputs:
def test_output_rev_upp():
    assert ru.rev_upp(1, 'Oliver') == 'OLIVER'
    assert ru.rev_upp(2, 'Oliver') == 'revilO'
    assert ru.rev_upp(3, 'Oliver') == 'REVILO'
    assert ru.rev_upp(2, 'Hello World') == 'dlroW olleH'
    assert ru.rev_upp(3, '#/,"') == '",/#'


# Rev upp invalid inputs:
def test_invalid_rev_upp():
    with pytest.raises(Exception):
        assert ru.rev_upp(123)
        assert ru.rev_upp(['Hello', 123])
        assert ru.rev_upp([1, 'Hello'])
        assert ru.rev_upp(3, 123)
        assert ru.rev_upp(4, 'Hello')
        assert ru.rev_upp(0, 'Hello')
        assert ru.rev_upp('Hello', 1)


# Rev valid inputs:
def test_output_rev():
    assert ru.rev('Oliver') == 'revilO'
    assert ru.rev('Hello World') == 'dlroW olleH'
    assert ru.rev('#/,"') == '",/#'


# Rev invalid inputs:
def test_invalid_rev():
    with pytest.raises(Exception):
        assert ru.rev([1, 'Hello'])
        assert ru.rev(['Hello', 123])
        assert ru.rev(123)
        assert ru.rev(3, 123)
        assert ru.rev(4, 'Hello')
        assert ru.rev(0, 'Hello')
        assert ru.rev('Hello', 1)


# Upp valid inputs:
def test_output_upp():
    assert ru.upp('Oliver') == 'OLIVER'
    assert ru.upp('Hello World') == 'HELLO WORLD'
    assert ru.upp('#/,"') == '#/,"'


# Upp invalid inputs:
def test_invalid_upp():
    with pytest.raises(Exception):
        assert ru.upp([1, 'Hello'])
        assert ru.upp(['Hello', 123])
        assert ru.upp(123)
        assert ru.upp(3, 123)
        assert ru.upp(4, 'Hello')
        assert ru.upp(0, 'Hello')
        assert ru.upp('Hello', 1)


# Rev_upp_file valid inputs:
def test_output_rev_upp_file():
    assert ru.rev_upp_file(chosen_option=1,
                           file_input="C:/Users/Oliver/PycharmProjects/Python"
                                      + "Boot/oo_pbc_pkg/README.md",
                           destination="C://Users//Oliver//PycharmProjects//"
                                       + "PythonBoot"
                           ) == '# OO_PBC_PKG\n\nTHIS IS A SIMPLE PYTHON BOOT CAMP PACKAGE. \n\nYOU CAN USE ITS MODULES TO REVERSE OR UPPERCASE STRINGS.'
    assert ru.rev_upp_file(chosen_option=3,
                           file_input="C:/Users/Oliver/PycharmProjects/Python"
                                      + "Boot/oo_pbc_pkg/README.md",
                           destination="C://Users//Oliver//PycharmProjects//"
                                       + "PythonBoot"
                           ) == '\nGKP_CBP_OO #\n\n .EGAKCAP PMAC TOOB NOHTYP ELPMIS A SI SIHT\n.SGNIRTS ESACREPPU RO ESREVER OT SELUDOM STI ESU NAC UOY'


# Rev_upp_file invalid inputs:
def test_invalid_rev_upp_file():
    with pytest.raises(Exception):
        assert ru.rev_upp_file(chosen_option=4,
                               file_input="C:/Users/Oliver/PycharmProjects/"
                                          + "PythonBoot/oo_pbc_pkg/README.md",
                               destination="C://Users//Oliver//PycharmProj"
                                           + "ects//PythonBoot"
                               )
        assert ru.rev_upp_file(chosen_option=1,
                               file_input="C:/Users/Oliver/PycharmProjects/"
                                          + "PythonBoot/oo_pbc_pkg/READM.md",
                               destination="C://Users//Oliver//PycharmProj"
                                           + "ects//PythonBoot"
                               )
        assert ru.rev_upp_file(chosen_option=3,
                               file_input="C:/Users/Oliver/PycharmProjects/"
                                          + "PythonBoot/oo_pbc_pkg/README.md",
                               destination="C://Users//Oliver//PycharmProj"
                                           + "ects//PythonBoo"
                               )
