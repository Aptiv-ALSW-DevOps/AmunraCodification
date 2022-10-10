import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
from script_helper import convert_string_to_bool


def test_convert_string_to_bool_test02():
    assert convert_string_to_bool('f') is False

    assert convert_string_to_bool(2) is None

    assert convert_string_to_bool('and') is None
