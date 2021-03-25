import os
from colorama import init, Fore, Style

init()
color_codes = {"0": Fore.BLACK,
               "1": Fore.BLUE,
               "2": Fore.LIGHTGREEN_EX,
               "3": Fore.CYAN,
               "4": Fore.RED,
               "5": Fore.MAGENTA,
               "6": Fore.YELLOW,
               "7": Fore.WHITE,
               "8": Fore.LIGHTBLACK_EX,
               "9": Fore.LIGHTBLUE_EX,
               "a": Fore.LIGHTGREEN_EX,
               "b": Fore.LIGHTCYAN_EX,
               "c": Fore.LIGHTRED_EX,
               "d": Fore.LIGHTMAGENTA_EX,
               "e": Fore.LIGHTYELLOW_EX,
               "f": Fore.LIGHTWHITE_EX,
               "g": Fore.YELLOW,
               "l": Style.BRIGHT
               }


def formatted(message):
    if "§" in message:
        final_message = ""
        split = message.split("§")
        for section in split:
            if section == "":
                continue
            formatted_section = f"{color_codes[section[0]]}{section[1:]}"
            if len(section) != 1:
                formatted_section += Style.RESET_ALL
            final_message += formatted_section
    else:
        if ">" not in message and "»" not in message:
            return message
        try:
            arrow = message.index(">")
            if "<" in message:
                arrow += 1
        except ValueError:
            arrow = message.index("»")
        final_message = f"{Fore.LIGHTCYAN_EX}{message[0:arrow]}{Fore.LIGHTBLACK_EX}{message[arrow]}{Fore.LIGHTWHITE_EX}{message[arrow+1:]}"
    return final_message


def chatlog():
    messages = []
    with open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r") as f:
        log = f.readlines()

    for line in log:
        if "[CHAT]" in line:
            message = line[line.index("C") + 6:len(line) - 1]
            messages.append(message)
    return messages


while True:
    prev_log = chatlog()
    while len(prev_log) == len(chatlog()):
        continue
    new_messages = chatlog()[len(prev_log):]
    for message in new_messages:
        print(formatted(message))
