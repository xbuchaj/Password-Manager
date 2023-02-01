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

def manager(t):
    os.system("mode con cols=60 lines=21")

    # Commands for drawing the graphic user interface
    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    for i in range(3, terminal.height - 5):
        print(terminal.move_xy(8, i) +  "║")
        print(terminal.move_xy((terminal.width - 9), i) +  "║")
        if i == 3:
            print(terminal.move_xy(21, i) +  "║")
        if i >= 5:
            print(terminal.move_xy(21, i) +  "║")
    for i in range(9, terminal.width - 9):
        print(terminal.move_xy(i, 2) +  "═")
        print(terminal.move_xy(i, 4) +  "═")
        print(terminal.move_xy(i, (terminal.height - 5)) +  "═")
    print(terminal.move_xy(8, 2) +  "╔")
    print(terminal.move_xy((terminal.width - 9), 2) +  "╗")
    print(terminal.move_xy(8, (terminal.height - 5)) +  "╚")
    print(terminal.move_xy((terminal.width - 9), (terminal.height - 5)) +  "╝")
    print(terminal.move_xy(12, 3) +  "DOMAIN")
    print(terminal.move_xy(28, 3) +  "USERNAME / E-MAIL")
    print(terminal.move_xy(9, (terminal.height - 3)) +  "EDIT")
    print(terminal.move_xy((terminal.width // 2) - 6, (terminal.height - 3)) +  "SHOW PASSWORD")
    print(terminal.move_xy((terminal.width - 15), (terminal.height - 3)) +  "DELETE")
    print(terminal.move_xy((terminal.width // 2) - 27, terminal.height) +  "↑↓→←: MOVE, N: CREATE NEW, Enter: SELECT, ESC: LOG OUT")

    # Variable (int) for position where is cursor
    pointer = 1
    lastPointer = None

    # Variable for output
    outputID = None

    while True:
        # Write domain names and usernames and draw the cursor in the list of domains
        if (pointer != lastPointer) and (pointer < (len(t) + 1)):
            lastPointer = pointer
            if pointer <= 6:
                for i in range(0, len(t)):
                    if i < 6:
                        print(terminal.move_xy(9, 4 + (i * 2)) +  t[i][2])
                        print(terminal.move_xy(22, 4 + (i * 2)) +  t[i][3])
                        for j in range(9, terminal.width - 9):
                            print(terminal.move_xy(j, 5 + (i * 2)) +  "═")
                print(terminal.cornflowerblue + terminal.on_white)
                print(terminal.move_xy(9, 4 + ((pointer - 1) * 2)) +  t[pointer - 1][2])
                print(terminal.white + terminal.on_cornflowerblue)

            if pointer > 6:
                j = -1
                for i in range(pointer - 6, len(t)):
                    j += 1
                    if i < pointer:
                        print(terminal.move_xy(9, 4 + (j * 2)) +  t[i][2])
                        print(terminal.move_xy(22, 4 + (j * 2)) +  t[i][3])
                        for k in range(9, terminal.width - 9):
                            print(terminal.move_xy(k, 5 + (j * 2)) +  "═")
                print(terminal.cornflowerblue + terminal.on_white)
                print(terminal.move_xy(9, 14) +  t[pointer - 1][2])
                print(terminal.white + terminal.on_cornflowerblue)
        
        # Draw the cursor in the select menu
        if pointer == (len(t) + 1):
            print(terminal.move_xy((terminal.width // 2) - 6, (terminal.height - 4)) +  "SHOW PASSWORD")
            print(terminal.move_xy((terminal.width - 15), (terminal.height - 4)) +  "DELETE")
            print(terminal.cornflowerblue + terminal.on_white)
            print(terminal.move_xy(9, (terminal.height - 4)) +  "EDIT")
            print(terminal.white + terminal.on_cornflowerblue)
        elif pointer == (len(t) + 2):
            print(terminal.move_xy(9, (terminal.height - 4)) +  "EDIT")
            print(terminal.move_xy((terminal.width - 15), (terminal.height - 4)) +  "DELETE")
            print(terminal.cornflowerblue + terminal.on_white)
            print(terminal.move_xy((terminal.width // 2) - 6, (terminal.height - 4)) +  "SHOW PASSWORD")
            print(terminal.white + terminal.on_cornflowerblue)
        elif pointer == (len(t) + 3):
            print(terminal.move_xy(9, (terminal.height - 4)) +  "EDIT")
            print(terminal.move_xy((terminal.width // 2) - 6, (terminal.height - 4)) +  "SHOW PASSWORD")
            print(terminal.cornflowerblue + terminal.on_white)
            print(terminal.move_xy((terminal.width - 15), (terminal.height - 4)) +  "DELETE")
            print(terminal.white + terminal.on_cornflowerblue)

        # Load the key immediately after press
        with terminal.cbreak():
            # Variable for code of key which was press
            val = terminal.inkey()
            
            # If wasn't press key with letter
            if val.is_sequence:

                # If was press the ESC key
                if val.code == 361:
                    return "logOut"

                # If was press ENTER key
                elif val.code == 343:
                    if pointer <= len(t):
                        outputID = t[pointer - 1][1]
                        pointer = len(t) + 2
                    elif pointer == (len(t) + 1):
                        return "edit", outputID
                    elif pointer == (len(t) + 2):
                        return "show", outputID
                    elif pointer == (len(t) + 3):
                        return "del", outputID

                # If was press RIGHT key
                elif val.code == 261:
                    if pointer > len(t):
                        if pointer < len(t) + 3:
                            pointer += 1
                        else:
                            pointer = len(t) + 1

                # If was press LEFT key
                elif val.code == 260:
                    if pointer > len(t):
                        if pointer > len(t) + 1:
                            pointer -= 1
                        else:
                            pointer = len(t) + 3

                # If was press UP key
                elif val.code == 259:
                    if pointer <= len(t):
                        if pointer > 1:
                            pointer -= 1
                        else:
                            pointer = len(t)
                
                # If was press DOWN key
                elif val.code == 258:
                    if pointer <= len(t):
                        if pointer < len(t):
                            pointer += 1
                        else:
                            pointer = 1
            
            # If was press key with letter
            else:
                if (val == 'n') or (val == 'N'):
                    return "create"

def addNew(error = False):
    os.system("mode con cols=60 lines=18")

    # Variables (string) for domain, username and password
    domain = ""
    username = ""
    password = ""

    # Commands for drawing the graphic user interface
    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 18, (terminal.height // 2) - 5) + terminal.bold +  "ADD NEW DOMAIN, USERNAME AND PASSWORD")
    print(terminal.move_xy((terminal.width // 2) - 6, terminal.height // 2 - 1) + terminal.bold +  "DOMAIN:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 1) +  "USERNAME:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 3) +  "PASSWORD:")
    if error == True:
        print(terminal.move_xy((terminal.width // 2) - 13, (terminal.height // 2) + 4) + terminal.red + "You must fill in all data.")
    print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 5) + terminal.white + "DONE")
    print(terminal.move_xy((terminal.width // 2) - 23, terminal.height) +  "↑↓: MOVE, Enter: SELECT, ESC: BACK TO MAIN MENU")

    # Variable (int) for position where is cursor
    pointer = 1
    while True:
        # Commands for drawing the cursor
        if pointer == 1:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4) +  "DONE")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(domain), (terminal.height // 2) - 2) +  "█")
        elif pointer == 2:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(domain), (terminal.height // 2) - 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  "█")
        elif pointer == 3:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4) +  "DONE")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  "█")
        else:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(domain), (terminal.height // 2) - 2) +  " ")
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
                    return "back"

                # If was press the BACKSPACE key
                elif val.code == 263:
                    if pointer == 1:
                        domain = domain[0: len(domain) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(domain), (terminal.height // 2) - 2) +  " ")
                    if pointer == 2:
                        username = username[0: len(username) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(username), terminal.height // 2) +  " ")
                    if pointer == 3:
                        password = password[0: len(password) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(password), (terminal.height // 2) + 2) +  " ")

                # If was press ENTER key
                elif val.code == 343:
                    if pointer < 3:
                        pointer += 1
                    elif pointer == 4:
                        return domain, username, password

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
                    domain = domain + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) - 2) +  domain)
                if pointer == 2:
                    username = username + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height // 2) +  username)
                if pointer == 3:
                    password = password + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) + 2) + len(password) * "*")

def showPassword(t):
    os.system("mode con cols=50 lines=10")

    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 17, (terminal.height - 7)) + "SHOW DOMAIN, USERNAME AND PASSWORD")
    print(terminal.move_xy((terminal.width // 2) - 6, (terminal.height - 5)) + "DOMAIN:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height - 4)) + "USERNAME:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height - 3)) + "PASSWORD:")
    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height - 5)) + t[2])
    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height - 4)) + t[3])
    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height - 3)) + t[4])
    print(terminal.move_xy((terminal.width // 2) - 15, terminal.height) +  "Enter / ESC: BACK TO MAIN MENU")

    while True:
        # Load the key immediately after press
        with terminal.cbreak():
            # Variable for code of key which was press
            val = terminal.inkey()
            
            # If wasn't press key with letter
            if val.is_sequence:

                # If was press the ESC key or ENTER key
                if (val.code == 361) or (val.code == 343):
                    break

def edit(t, error = False):
    os.system("mode con cols=60 lines=18")

    # Variables (string) for domain, username and password
    domain = t[2]
    username = t[3]
    password = t[4]

    # Commands for drawing the graphic user interface
    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 19, (terminal.height // 2) - 5) + terminal.bold +  "EDIT DOMAIN NAME, USERNAME OR PASSWORD")
    print(terminal.move_xy((terminal.width // 2) - 6, terminal.height // 2 - 1) + terminal.bold +  "DOMAIN:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 1) +  "USERNAME:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 3) +  "PASSWORD:")
    if error == True:
        print(terminal.move_xy((terminal.width // 2) - 13, (terminal.height // 2) + 4) + terminal.red + "You must fill in all data.")
    print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 5) + terminal.white + "DONE")
    print(terminal.move_xy((terminal.width // 2) - 23, terminal.height) +  "↑↓: MOVE, Enter: SELECT, ESC: BACK TO MAIN MENU")
    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) - 2) +  domain)
    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height // 2) +  username)
    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) + 2) + len(password) * "*")

    # Variable (int) for position where is cursor
    pointer = 1
    while True:
        # Commands for drawing the cursor
        if pointer == 1:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4) +  "DONE")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(domain), (terminal.height // 2) - 2) +  "█")
        elif pointer == 2:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(domain), (terminal.height // 2) - 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  "█")
        elif pointer == 3:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(username), terminal.height // 2) +  " ")
            print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 4) +  "DONE")
            print(terminal.move_xy((terminal.width // 2) + 2 + len(password), (terminal.height // 2) + 2) +  "█")
        else:
            print(terminal.move_xy((terminal.width // 2) + 2 + len(domain), (terminal.height // 2) - 2) +  " ")
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
                    return "back"

                # If was press the BACKSPACE key
                elif val.code == 263:
                    if pointer == 1:
                        domain = domain[0: len(domain) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(domain), (terminal.height // 2) - 2) +  " ")
                    if pointer == 2:
                        username = username[0: len(username) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(username), terminal.height // 2) +  " ")
                    if pointer == 3:
                        password = password[0: len(password) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(password), (terminal.height // 2) + 2) +  " ")

                # If was press ENTER key
                elif val.code == 343:
                    if pointer < 3:
                        pointer += 1
                    elif pointer == 4:
                        return domain, username, password

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
                    domain = domain + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) - 2) +  domain)
                if pointer == 2:
                    username = username + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height // 2) +  username)
                if pointer == 3:
                    password = password + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) + 2) + len(password) * "*")