import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
from script_helper import convert_string_to_bool

def test_convert_string_to_bool_test01():
    test_1 = ["true","1","t","y","yes"]
    output = convert_string_to_bool(test_1)
    assert output is True

def test_convert_string_to_bool_test06():
    output = convert_string_to_bool("false")
    assert output is False

def test_convert_string_to_bool_test07():
    output = convert_string_to_bool("0")
    assert output is False

def test_convert_string_to_bool_test08():
    output = convert_string_to_bool("f")
    assert output is False

def test_convert_string_to_bool_test09():
    output = convert_string_to_bool("n")
    assert output is False

def test_convert_string_to_bool_test10():
    output = convert_string_to_bool("no")
    assert output is False












    
