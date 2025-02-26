import sys
from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.divide import DivideCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()


    def start(self):
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop

            command_line_input = input(">>> ").strip()
            if command_line_input == 'exit':
                print("Exiting Command line")
                sys.exit(1)
            if(len(command_line_input.split())) != 3:
                print("Usage : <number1> <number2> <operation>")
                continue
            
            num1, num2, operation = command_line_input.split()
            self.command_handler.execute_command(operation, num1, num2)



