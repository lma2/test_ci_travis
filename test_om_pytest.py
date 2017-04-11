'''
Test other_math with pytest
To run tests : py.test             test_om_pytest.py
          or : python -m pytest    test_om_pytest.py
Verobse (-v) : py.test -v          test_om_pytest.py
          or : python -m pytest -v test_om_pytest.py
'''

from other_math import multiply

def test_numbers_3_4():
    """Test multiply in numbers"""
    assert multiply(3, 4) == 12

def test_strings_a_3():
    """Test multiply in strings"""
    assert multiply('a', 3) == 'aaa'
