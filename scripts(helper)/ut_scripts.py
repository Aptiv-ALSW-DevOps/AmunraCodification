import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
from script_helper import convert_string_to_bool

def test_convert_string_to_bool_test01():
    output = convert_string_to_bool("true")
    assert output is True

def test_convert_string_to_bool_test02():
    output = convert_string_to_bool("1")
    assert output is True

def test_convert_string_to_bool_test03():
    output = convert_string_to_bool("t")
    assert output is True

def test_convert_string_to_bool_test04():
    output = convert_string_to_bool("y")
    assert output is True

def test_convert_string_to_bool_test05():
    output = convert_string_to_bool("yes")
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

def test_convert_string_to_bool_test11():
    output = convert_string_to_bool((type(int)))
    assert output is None









    
