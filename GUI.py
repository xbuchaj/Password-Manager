import blessed
import os

terminal = blessed.Terminal()

def logIn(error = False):
    os.system("mode con cols=60 lines=21")
    # Variables (string) for username and password
    username = ""
    password = ""

    # Commands for drawing the graphic user interface
    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) - 5) + terminal.bold +  "PASSWORD MANAGER")
    print(terminal.move_xy((terminal.width // 2) - 3, terminal.height // 2 - 1) + terminal.bold +  "LOG IN")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 1) +  "USERNAME:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 3) +  "PASSWORD:")
    if error == True:
        print(terminal.move_xy((terminal.width // 2) - 13, (terminal.height // 2) + 4) + terminal.red + "Wrong username or password")
    print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 5) + terminal.white + "DONE")
    print(terminal.move_xy((terminal.width // 2) - 15, (terminal.height // 2) + 7) +  "I want to create new account!")
    print(terminal.move_xy((terminal.width // 2) - 17, terminal.height) +  "↑↓: MOVE, Enter: SELECT, ESC: Quit")

    # Variable (int) for position where is cursor
    pointer = 1
    while True:
        # Commands for drawing the cursor
        if pointer == 1:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) - 15, (terminal.height // 2) + 6) +  "I want to create new account!")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  "█")
        elif pointer == 2:
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4) +  "DONE")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  "█")
        elif pointer == 3:
            print(terminal.move_xy((terminal.width // 2) - 15, (terminal.height // 2) + 6) +  "I want to create new account!")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  " ")
            print(terminal.cornflowerblue + terminal.on_white)
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4)  +  "DONE")
            print(terminal.white + terminal.on_cornflowerblue)
        else:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4) +  "DONE")
            print(terminal.cornflowerblue + terminal.on_white)
            print(terminal.move_xy((terminal.width // 2) - 15, (terminal.height // 2) + 6) +  "I want to create new account!")
            print(terminal.white + terminal.on_cornflowerblue)

        # Load the key immediately after press
        with terminal.cbreak():
            # Variable for code of key which was press
            val = terminal.inkey()
            
            # If wasn't press key with letter
            if val.is_sequence:

                # If was press the ESC key
                if val.code == 361:
                    quit()

                # If was press the BACKSPACE key
                elif val.code == 263:
                    if pointer == 1:
                        username = username[0: len(username) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(username), terminal.height // 2) +  " ")
                    if pointer == 2:
                        password = password[0: len(password) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(password), (terminal.height // 2) + 2) +  " ")

                # If was press ENTER key
                elif val.code == 343:
                    if pointer < 3:
                        pointer += 1
                    elif pointer == 3:
                        return username, password
                    elif pointer == 4:
                        return "new_account"

                # If was press UP key
                elif val.code == 259:
                    if pointer == 1:
                        pointer = 4
                    elif pointer == 2:
                        pointer = 1
                    elif pointer == 3:
                        pointer = 2
                    elif pointer == 4:
                        pointer = 3
                
                # If was press DOWN key
                elif val.code == 258:
                    if pointer == 1:
                        pointer = 2
                    elif pointer == 2:
                        pointer = 3
                    elif pointer == 3:
                        pointer = 4
                    elif pointer == 4:
                        pointer = 1  

            # If was press key with letter
            else:
                if pointer == 1:
                    username = username + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height // 2) +  username)
                if pointer == 2:
                    password = password + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) + 2) + len(password) * "*")

def signIn(error = False):
    os.system("mode con cols=60 lines=21")
    # Variables (string) for username and password
    username = ""
    password = ""

    # Commands for drawing the graphic user interface
    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) - 5) + terminal.bold +  "PASSWORD MANAGER")
    print(terminal.move_xy((terminal.width // 2) - 9, terminal.height // 2 - 1) + terminal.bold +  "CREATE NEW ACCOUNT")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 1) +  "USERNAME:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 3) +  "PASSWORD:")
    if error == True:
        print(terminal.move_xy((terminal.width // 2) - 28, (terminal.height // 2) + 4) + terminal.red + "Username or password is inappropriate or already exists")
    print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 5) + terminal.white + "DONE")
    print(terminal.move_xy((terminal.width // 2) - 17, terminal.height) +  "↑↓: MOVE, Enter: SELECT, ESC: Quit")

    # Variable (int) for position where is cursor
    pointer = 1
    while True:
        # Commands for drawing the cursor
        if pointer == 1:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4) +  "DONE")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  "█")
        elif pointer == 2:
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4) +  "DONE")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  "█")
        else:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  " ")
            print(terminal.cornflowerblue + terminal.on_white)
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4)  +  "DONE")
            print(terminal.white + terminal.on_cornflowerblue)

        # Load the key immediately after press
        with terminal.cbreak():
            # Variable for code of key which was press
            val = terminal.inkey()
            
            # If wasn't press key with letter
            if val.is_sequence:

                # If was press the ESC key
                if val.code == 361:
                    quit()

                # If was press the BACKSPACE key
                elif val.code == 263:
                    if pointer == 1:
                        username = username[0: len(username) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(username), terminal.height // 2) +  " ")
                    if pointer == 2:
                        password = password[0: len(password) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(password), (terminal.height // 2) + 2) +  " ")

                # If was press ENTER key
                elif val.code == 343:
                    if pointer < 3:
                        pointer += 1
                    elif pointer == 3:
                        return username, password

                # If was press UP key
                elif val.code == 259:
                    if pointer == 1:
                        pointer = 3
                    elif pointer == 2:
                        pointer = 1
                    elif pointer == 3:
                        pointer = 2
                
                # If was press DOWN key
                elif val.code == 258:
                    if pointer == 1:
                        pointer = 2
                    elif pointer == 2:
                        pointer = 3
                    elif pointer == 3:
                        pointer = 1

            # If was press key with letter
            else:
                if pointer == 1:
                    username = username + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height // 2) +  username)
                if pointer == 2:
                    password = password + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) + 2) + len(password) * "*")