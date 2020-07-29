import math_func
import pytest
import sys

@pytest.mark.number
def test_add():
    assert math_func.add(7,3)==10
    assert math_func.add(5,2)==7
    assert math_func.add(3)==5

@pytest.mark.skip(reason="do not run this test")
def test_product():
    assert math_func.product(5,2)==10
    assert math_func.product(2)==3
@pytest.mark.skipif(sys.version_info<(3, 8),reason="do not run this test")
def test_add_strings():
    result = math_func.add('Hello','World')
    assert result=='HelloWorld'
    assert type(result)==str
    assert 'Heldio' not in result
