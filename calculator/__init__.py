from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
    
class Calculator:
    @staticmethod
    def _perform_operaration(a:Decimal,b:Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        '''create and perform a calcualtion, then return result'''
        calculation = Calculation.create(a,b,operation)
        Calculations.add_calculation_to_history(calculation)
        return calculation.perform()

    @staticmethod
    def add(a:Decimal,b:Decimal) -> Decimal:
        return Calculator._perform_operaration(a,b,add)

    @staticmethod
    def subtract(a:Decimal,b:Decimal) -> Decimal:
        return Calculator._perform_operaration(a,b,subtract)
    
    @staticmethod
    def multiply(a:Decimal,b:Decimal) -> Decimal:
        return Calculator._perform_operaration(a,b,multiply)
    
    @staticmethod
    def divide(a:Decimal,b:Decimal) -> Decimal:
        return Calculator._perform_operaration(a,b,divide)