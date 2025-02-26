import importlib
import sys
import pkgutil
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        self.load_plugins()
        # Register commands here - now its dynamically loading
        # self.command_handler.register_command("add", AddCommand())
        # self.command_handler.register_command("subtract", SubtractCommand())
        # self.command_handler.register_command("multiply", MultiplyCommand())
        # self.command_handler.register_command("divide", DivideCommand())

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



