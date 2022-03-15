import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

from utils import *
from .functions import *


def Script():
    attributes = ["mental + 3"]
    t = task.Task("Reading", *attributes)
    
    '''while True:
        init_command = delay_input(f"Enter a command(type 'help' for assistance): ")
        if init_command == 'help':
            delay_print()'''
