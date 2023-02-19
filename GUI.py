'''
          GUI.py - beta1.0 - developed by xbuchaj in 2023
This source code contains functions for creating a user environment for 
the Password Manager application using the terminal. For better graphic 
editing, the blessed 1.20.00 library and the os library are used.
This version of the code corresponds to version 1.0, so if some 
functionalities do not work correctly, I will work on removing them. 
And at the same time, I plan to improve the graphic side of the mentioned 
application in the future.

LICENSE:
Copyright 2023 @xbuchaj
Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.
'''

import blessed
import os

terminal = blessed.Terminal()

def logIn(error = False):
    '''
    A function that creates a user interface for user login. In this interface, 
    it is possible to move using the down and up keys, confirm the entered data 
    with the enter key and close the entire application with the esc key.
    Parameters:
        error (bool): If the parameter is equal to the logical value FALSE, the 
        error message will not be displayed, but if it is TRUE, it will be 
        displayed.
    '''
    os.system("mode con cols=60 lines=21")

    username = ""
    password = ""

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

    pointer = 1
    while True:

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

        with terminal.cbreak():
            val = terminal.inkey()
            
            if val.is_sequence:

                if val.code == 361:
                    quit()

                elif val.code == 263:
                    if pointer == 1:
                        username = username[0: len(username) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(username), terminal.height // 2) +  " ")
                    if pointer == 2:
                        password = password[0: len(password) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(password), (terminal.height // 2) + 2) +  " ")

                elif val.code == 343:
                    if pointer < 3:
                        pointer += 1
                    elif pointer == 3:
                        return username, password
                    elif pointer == 4:
                        return "new_account"

                elif val.code == 259:
                    if pointer == 1:
                        pointer = 4
                    elif pointer == 2:
                        pointer = 1
                    elif pointer == 3:
                        pointer = 2
                    elif pointer == 4:
                        pointer = 3
                
                elif val.code == 258:
                    if pointer == 1:
                        pointer = 2
                    elif pointer == 2:
                        pointer = 3
                    elif pointer == 3:
                        pointer = 4
                    elif pointer == 4:
                        pointer = 1  

            else:
                if pointer == 1:
                    username = username + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height // 2) +  username)
                if pointer == 2:
                    password = password + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) + 2) + len(password) * "*")

def signIn(error = False):
    '''
    A function that creates a user interface for user registration. In this 
    interface, it is possible to move using the down and up keys, confirm 
    the entered data with the enter key and close the entire application with 
    the esc key.
    Parameters:
        error (bool): If the parameter is equal to the logical value FALSE, the 
        error message will not be displayed, but if it is TRUE, it will be 
        displayed.
    '''
    os.system("mode con cols=60 lines=21")

    username = ""
    password = ""

    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) - 5) + terminal.bold +  "PASSWORD MANAGER")
    print(terminal.move_xy((terminal.width // 2) - 9, terminal.height // 2 - 1) + terminal.bold +  "CREATE NEW ACCOUNT")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 1) +  "USERNAME:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 3) +  "PASSWORD:")
    if error == True:
        print(terminal.move_xy((terminal.width // 2) - 28, (terminal.height // 2) + 4) + terminal.red + "Username or password is inappropriate or already exists")
    print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 5) + terminal.white + "DONE")
    print(terminal.move_xy((terminal.width // 2) - 17, terminal.height) +  "↑↓: MOVE, Enter: SELECT, ESC: Quit")

    pointer = 1
    while True:

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

        with terminal.cbreak():
           
            val = terminal.inkey()
            
            if val.is_sequence:

                if val.code == 361:
                    quit()

                elif val.code == 263:
                    if pointer == 1:
                        username = username[0: len(username) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(username), terminal.height // 2) +  " ")
                    if pointer == 2:
                        password = password[0: len(password) - 1]
                        print(terminal.move_xy((terminal.width // 2) + 3 + len(password), (terminal.height // 2) + 2) +  " ")

                elif val.code == 343:
                    if pointer < 3:
                        pointer += 1
                    elif pointer == 3:
                        return username, password

                elif val.code == 259:
                    if pointer == 1:
                        pointer = 3
                    elif pointer == 2:
                        pointer = 1
                    elif pointer == 3:
                        pointer = 2
                
                elif val.code == 258:
                    if pointer == 1:
                        pointer = 2
                    elif pointer == 2:
                        pointer = 3
                    elif pointer == 3:
                        pointer = 1

            else:
                if pointer == 1:
                    username = username + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height // 2) +  username)
                if pointer == 2:
                    password = password + format(val)
                    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) + 2) + len(password) * "*")

def manager(t):
    '''A function that creates a user interface for the main part of the application. 
    In this section, the user can browse, create and manage records of his accounts. 
    The up and down keys are used to move in the main list, and to access the record 
    management, the record must be confirmed with the enter key. The left and right 
    keys are used between the actions that the user wants to perform with the given 
    record. The user confirms the selection of the action with the enter key. To create 
    a new record, the user presses the N key.
    Parameters:
        t (list): A list containing the decrypted data of the logged-in user's records.
    '''
    os.system("mode con cols=60 lines=21")

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

    pointer = 1
    lastPointer = None

    outputID = None

    while True:
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

        with terminal.cbreak():
            val = terminal.inkey()
            
            if val.is_sequence:

                if val.code == 361:
                    return "logOut"

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

                elif val.code == 261:
                    if pointer > len(t):
                        if pointer < len(t) + 3:
                            pointer += 1
                        else:
                            pointer = len(t) + 1

                elif val.code == 260:
                    if pointer > len(t):
                        if pointer > len(t) + 1:
                            pointer -= 1
                        else:
                            pointer = len(t) + 3

                elif val.code == 259:
                    if pointer <= len(t):
                        if pointer > 1:
                            pointer -= 1
                        else:
                            pointer = len(t)
                
                elif val.code == 258:
                    if pointer <= len(t):
                        if pointer < len(t):
                            pointer += 1
                        else:
                            pointer = 1
            
            else:
                if (val == 'n') or (val == 'N'):
                    return "create"

def addNew(error = False):
    '''
    A function that creates a user interface for add new record. In this 
    interface, it is possible to move using the down and up keys, confirm 
    the entered data with the enter key and go back to the main menu of 
    application with the esc key.
    Parameters:
        error (bool): If the parameter is equal to the logical value FALSE, the 
        error message will not be displayed, but if it is TRUE, it will be 
        displayed.
    '''
    os.system("mode con cols=60 lines=18")

    domain = ""
    username = ""
    password = ""

    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 18, (terminal.height // 2) - 5) + terminal.bold +  "ADD NEW DOMAIN, USERNAME AND PASSWORD")
    print(terminal.move_xy((terminal.width // 2) - 6, terminal.height // 2 - 1) + terminal.bold +  "DOMAIN:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 1) +  "USERNAME:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 3) +  "PASSWORD:")
    if error == True:
        print(terminal.move_xy((terminal.width // 2) - 13, (terminal.height // 2) + 4) + terminal.red + "You must fill in all data.")
    print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 5) + terminal.white + "DONE")
    print(terminal.move_xy((terminal.width // 2) - 23, terminal.height) +  "↑↓: MOVE, Enter: SELECT, ESC: BACK TO MAIN MENU")

    pointer = 1
    while True:
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

        with terminal.cbreak():
            val = terminal.inkey()
            
            if val.is_sequence:

                if val.code == 361:
                    return "back"

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

                elif val.code == 343:
                    if pointer < 3:
                        pointer += 1
                    elif pointer == 4:
                        return domain, username, password

                elif val.code == 259:
                    if pointer == 1:
                        pointer = 4
                    elif pointer == 2:
                        pointer = 1
                    elif pointer == 3:
                        pointer = 2
                    elif pointer == 4:
                        pointer = 3
                
                elif val.code == 258:
                    if pointer == 1:
                        pointer = 2
                    elif pointer == 2:
                        pointer = 3
                    elif pointer == 3:
                        pointer = 4
                    elif pointer == 4:
                        pointer = 1
            
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
    '''
    A function that creates a user interface for show password. In this 
    interface, it is possible go back to the main menu of application 
    with the esc key.
    Parameters:
        t (list): A list containing the decrypted record which user selected
        in main menu.
    '''
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
        with terminal.cbreak():
            val = terminal.inkey()
            
            if val.is_sequence:

                if (val.code == 361) or (val.code == 343):
                    break

def edit(t):
    '''
    A function that creates a user interface for edit existing record. In this 
    interface, it is possible to move using the down and up keys, confirm 
    the entered data with the enter key and go back to the main menu of 
    application with the esc key.
    This user interface is very similar to the interface for creating a new record. 
    The only difference is that in this case the data is already pre-filled with 
    existing data.
    Parameters:
        t (list): A list containing the decrypted record which user selected
        in main menu.
    '''
    os.system("mode con cols=60 lines=18")

    domain = t[2]
    username = t[3]
    password = t[4]

    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 19, (terminal.height // 2) - 5) + terminal.bold +  "EDIT DOMAIN NAME, USERNAME OR PASSWORD")
    print(terminal.move_xy((terminal.width // 2) - 6, terminal.height // 2 - 1) + terminal.bold +  "DOMAIN:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 1) +  "USERNAME:")
    print(terminal.move_xy((terminal.width // 2) - 8, (terminal.height // 2) + 3) +  "PASSWORD:")
    # if error == True:
        # print(terminal.move_xy((terminal.width // 2) - 13, (terminal.height // 2) + 4) + terminal.red + "You must fill in all data.")
    print(terminal.move_xy((terminal.width // 2) - 2, (terminal.height // 2) + 5) + terminal.white + "DONE")
    print(terminal.move_xy((terminal.width // 2) - 23, terminal.height) +  "↑↓: MOVE, Enter: SELECT, ESC: BACK TO MAIN MENU")
    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) - 2) +  domain)
    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height // 2) +  username)
    print(terminal.move_xy((terminal.width // 2) + 2, (terminal.height // 2) + 2) + len(password) * "*")

    pointer = 1
    while True:
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

        with terminal.cbreak():
            val = terminal.inkey()
            
            if val.is_sequence:

                if val.code == 361:
                    return "pass"

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

                elif val.code == 343:
                    if pointer < 3:
                        pointer += 1
                    elif pointer == 4:
                        return domain, username, password

                elif val.code == 259:
                    if pointer == 1:
                        pointer = 4
                    elif pointer == 2:
                        pointer = 1
                    elif pointer == 3:
                        pointer = 2
                    elif pointer == 4:
                        pointer = 3
                
                elif val.code == 258:
                    if pointer == 1:
                        pointer = 2
                    elif pointer == 2:
                        pointer = 3
                    elif pointer == 3:
                        pointer = 4
                    elif pointer == 4:
                        pointer = 1
            
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

def delete(t):
    '''
    A function that creates a user interface for a message if the user really wants 
    to delete his record. The user can navigate the interface using the left and 
    right keys, and can return to the main menu with the esc key.
    Parameters:
        t (list): A list containing the decrypted record which user selected
        in main menu.
    '''
    os.system("mode con cols=50 lines=9")

    domain = t[2]

    print(terminal.home + terminal.on_cornflowerblue + terminal.clear)
    print(terminal.move_xy((terminal.width // 2) - 14, terminal.height - 7) + terminal.bold +  "DO YOU WANT REALLY DELETE IT?")
    print(terminal.move_xy((terminal.width // 2) - 11, terminal.height - 5) + terminal.bold +  "DOMAIN NAME:")
    print(terminal.move_xy((terminal.width // 2) + 2, terminal.height - 5) + terminal.bold +  domain)
    print(terminal.move_xy((terminal.width // 2) - 6, terminal.height - 3) +  "YES")
    print(terminal.move_xy((terminal.width // 2) + 3, terminal.height - 3) +  "NO")
    print(terminal.move_xy((terminal.width // 2) - 23, terminal.height) +  "→←: MOVE, Enter: SELECT, ESC: BACK TO MAIN MENU")

    pointer = 2
    while True:
        if pointer == 1:
            print(terminal.move_xy((terminal.width // 2) + 3, terminal.height - 4) +  "NO")
            print(terminal.cornflowerblue + terminal.on_white)
            print(terminal.move_xy((terminal.width // 2) - 6, terminal.height - 4) +  "YES")
            print(terminal.white + terminal.on_cornflowerblue)
        elif pointer == 2:
            print(terminal.move_xy((terminal.width // 2) - 6, terminal.height - 4) +  "YES")
            print(terminal.cornflowerblue + terminal.on_white)
            print(terminal.move_xy((terminal.width // 2) + 3, terminal.height - 4) +  "NO")
            print(terminal.white + terminal.on_cornflowerblue)
        
        with terminal.cbreak():
            val = terminal.inkey()
            
            if val.is_sequence:

                if val.code == 361:
                    return "pass"
                
                elif val.code == 343:
                    if pointer == 1:
                        return "delete"
                    else:
                        return "pass"

                elif (val.code == 261) or (val.code == 260):
                    if pointer == 1:
                        pointer = 2
                    else:
                        pointer = 1