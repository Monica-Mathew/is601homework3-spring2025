from abc import ABC, abstractmethod
import logging

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str,num1, num2):
        try:
            command = self.commands[command_name]
            command.execute(num1, num2)
        except KeyError:
            logging.info("Application usage - incorrect command")
            print(f"No such command: {command_name}")

