import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

from utils import *
from .functions import *


def Script():
    t = task.Task('test', 5)
    t.create_task()
    '''while True:
        init_command = delay_input(f"Enter a command(type 'help' for assistance): ")
        if init_command == 'help':
            delay_print()'''
