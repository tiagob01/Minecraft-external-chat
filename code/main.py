import os
import random
from colorama import init, Fore, Style

init()
user_colors = {}
user_color_types = [
    Fore.YELLOW,
    Fore.RED,
    Fore.GREEN,
    Fore.WHITE,
    Fore.CYAN,
    Fore.BLUE,
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTBLUE_EX,
    Fore.MAGENTA,
    Fore.BLACK
]
color_codes = {
    "0": Fore.BLACK,
    "1": Fore.BLUE,
    "2": Fore.GREEN,
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
    "l": Style.BRIGHT,
    "k": "📜",
    "r": Style.RESET_ALL
}


def formatted(message):
    if "§" in message:
        final_message = ""
        split = message.split("§")
        for section in split:
            if section.isspace() or section == "":
                continue
            formatted_section = f"{color_codes[section[0]]}{section[1:]}"
            if len(section) != 1:
                formatted_section += Style.RESET_ALL
            final_message += formatted_section
    else:
        if ">" not in message and "»" not in message and ":" not in message:
            final_message = f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{message}{Style.RESET_ALL}"
        else:
            try:
                arrow_i = message.index(">")
                if "<" in message[0]:
                    arrow_i += 1
            except ValueError:
                try:
                    arrow_i = message.index("»")
                except ValueError:
                    arrow_i = message.index(":")
            user = message[0:arrow_i]
            arrow = message[arrow_i]
            content = message[arrow_i+1]
            if user not in user_colors.keys():
                user_colors[user] = random.choice(user_color_types)

            final_message = f"{user_colors[user]}{user}{Fore.WHITE}{arrow}{Fore.LIGHTWHITE_EX}{content}{Style.RESET_ALL}"
    return final_message


def chatlog():
    messages = []
    try:
        with open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r") as f:
            log = f.readlines()
    except PermissionError:
        return chatlog()
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
