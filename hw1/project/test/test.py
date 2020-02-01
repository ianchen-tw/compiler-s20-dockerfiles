#! /usr/bin/env python3
import os
import time
# from sys import stderr

from colorama import init as colorama_init
from colorama import Fore, Back, Style

colorama_init()


def green_banner(text) -> str:
    return f'{Back.GREEN}{Fore.BLACK}{text}{Style.RESET_ALL}'
def red_banner(text) -> str:
    return f'{Back.RED}{Fore.BLACK}{text}{Style.RESET_ALL}'



print(green_banner('TEST'))
os.system('diff ./testcase/answer ./testcase/output')
print(red_banner('Oops!'))