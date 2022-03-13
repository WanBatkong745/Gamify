import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

from utils import *
from .functions import *


def Script():
    attributes = ["physical + 4", "health + 7", ]
    t = task.Task("jumping", *attributes)
    
    
    '''while True:
        init_command = delay_input(f"Enter a command(type 'help' for assistance): ")
        if init_command == 'help':
            delay_print()'''
