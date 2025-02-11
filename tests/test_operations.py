from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def create_Calculation_Instance(a,b,operation):
    calculation = Calculation.create(Decimal(a),Decimal(b),operation)
    return calculation

def test_operation_add():
    '''Testing the adding operation'''
    assert create_Calculation_Instance(10,5,add).perform() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    assert create_Calculation_Instance(10,5,subtract).perform() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    assert create_Calculation_Instance(10,5,multiply).perform() == Decimal('50'), "multiply operation failed"

def test_operation_divide():
    '''Testing the divison operation'''
    assert create_Calculation_Instance(10,5,divide).perform() == Decimal('2'), "divide operation failed"