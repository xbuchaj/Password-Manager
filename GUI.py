import blessed
import os

terminal = blessed.Terminal()
os.system("mode con cols=60 lines=21")

def logIn():
    username = ""
    password = ""
    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) - 5) + terminal.bold +  "PASSWORD MANAGER")
    print(terminal.move_xy((terminal.width // 2) - 3, terminal.height // 2 - 1) + terminal.bold +  "LOG IN")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 1) +  "USERNAME:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 3) +  "PASSWORD:")
    print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 5) +  "DONE")
    print(terminal.move_xy((terminal.width // 2) - 11, terminal.height) +  "Tab: MOVE, Enter: SELECT")
    pointer = 1
    while True:
        with terminal.cbreak():
            val = terminal.inkey()
            if val.is_sequence:
                if val.code == 263:
                    if pointer == 1:
                        username = username[0: len(username) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  " ")
                    if pointer == 2:
                        password = password[0: len(password) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  " ")
                elif pointer < 3:
                    if (val.code == 512) or (val.code == 343):
                        pointer += 1
                elif pointer == 3:
                    if val.code == 343:
                        return username, password
                    elif val.code == 512:
                        pointer = 1
                if pointer > 3:
                    pointer = 1
            else:
                if pointer == 1:
                    username = username + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height // 2) +  username)
                if pointer == 2:
                    password = password + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) + 2) + len(password) * "*")