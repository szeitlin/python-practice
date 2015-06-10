__author__ = 'szeitlin'

from func_limited_bubble import
from hypothesis import given
from hypothesis.strategies import lists, integers
from math import isnan

@given(lists(), integers())
def test_given_list_gives_expected_output(x):
    assume(not isnan(x))
    assert