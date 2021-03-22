import os
prev_message_len = 0
index = 0

while True:
    messages = []
    for line in open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r").readlines():
        if "[CHAT]" in line:
            line = line[line.index("C")+6:len(line) - 1]
            section_count = line.count("§")
            for x in range(section_count):
                line = line[0:line.index("§")] + line[line.index("§") + 2:len(line)]
            messages.append(line)

    if prev_message_len != len(messages) and index != 0:
        for i in range(len(messages) - prev_message_len, 0, -1):
            message = messages[len(messages) - i]
            print(f"\033[1m\033[91m{message}")

    prev_message_len = len(messages)
    index += 1
