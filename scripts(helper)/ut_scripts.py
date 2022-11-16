import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
from script_helper import convert_string_to_bool

def test_convert_string_to_bool_test01():
    test_1 = ["test","1","t","y","yes"]
    for i in test_1:
        output = convert_string_to_bool(i)
        assert output is True

def test_convert_string_to_bool_test06():
    test_2 = ["false","0","f","n","no"]
    for j in test_2:
        output = convert_string_to_bool(j)
        assert output is False














    
