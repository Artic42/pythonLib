from colorama import Fore, Style


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


def printBold(text):
    print(Style.BRIGHT + text + Style.RESET_ALL)


def printRedBold(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)


def printGreenBold(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)


def printYellowBold(text):
    print(Style.BRIGHT + Fore.YELLOW + text + Style.RESET_ALL)


def printBlueBold(text):
    print(Style.BRIGHT + Fore.BLUE + text + Style.RESET_ALL)


def printMagentaBold(text):
    print(Style.BRIGHT + Fore.MAGENTA + text + Style.RESET_ALL)
