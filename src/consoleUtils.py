import colorama
from colorama import Fore, Back, Style

def printRed(text):
    print(Fore.RED + text + Style.RESET_ALL)

def printGreen(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def printYellow(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

def printBlue(text):
    print(Fore.BLUE + text + Style.RESET_ALL)

def printMagenta(text):
    print(Fore.MAGENTA + text + Style.RESET_ALL)
    