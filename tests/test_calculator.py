'''My calculator test'''
from calculator import add, subtact

def test_addition():
    '''Test that additon function works'''
    assert add(2,2) ==4

def test_subtraction():
    '''Test that subtraction function works'''
    assert subtact(2,2) ==0
    