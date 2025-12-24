from colorama import Fore, Style


def printRed(text: str) -> None:
    print(Fore.RED + text + Style.RESET_ALL)


def printGreen(text: str) -> None:
    print(Fore.GREEN + text + Style.RESET_ALL)


def printYellow(text: str) -> None:
    print(Fore.YELLOW + text + Style.RESET_ALL)


def printBlue(text: str) -> None:
    print(Fore.BLUE + text + Style.RESET_ALL)


def printMagenta(text: str) -> None:
    print(Fore.MAGENTA + text + Style.RESET_ALL)


def printBold(text: str) -> None:
    print(Style.BRIGHT + text + Style.RESET_ALL)


def printRedBold(text: str) -> None:
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)


def printGreenBold(text: str) -> None:
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)


def printYellowBold(text: str) -> None:
    print(Style.BRIGHT + Fore.YELLOW + text + Style.RESET_ALL)


def printBlueBold(text: str) -> None:
    print(Style.BRIGHT + Fore.BLUE + text + Style.RESET_ALL)


def printMagentaBold(text: str) -> None:
    print(Style.BRIGHT + Fore.MAGENTA + text + Style.RESET_ALL)
