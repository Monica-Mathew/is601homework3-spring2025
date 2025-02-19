import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_print(a,b, operation_name):
    operation_mappings ={
        'add' : Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    
    }

def main():
    if(len(sys.argv)) != 4:
        print("Usage :python calculator _main.py <number1> <number2> <operation")
        sys.exit(1)

    _,a,b,operation = sys.argv
    calculate_and_print(a,b,operation)

if __name__ =='__main__':
    main()