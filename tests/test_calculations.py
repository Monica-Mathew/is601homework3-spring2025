'''My calculations test'''
from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test that additon function works'''
    assert add(2,2) ==4

def test_subtraction():
    '''Test that subtraction function works'''
    assert subtract(2,2) ==0

def test_multiply():
    '''Test that multiply function works'''
    assert multiply(2,2) == 4

def test_divide():
    '''Test that divide function works'''
    assert divide(2,2) ==1
