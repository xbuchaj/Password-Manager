'''
            main.py - v1.0 - developed by xbuchaj in 2023
This source code contains the backend for the entire Password Manager 
application. The program stores data entered by users in csv files. 
User.csv contains information about user accounts and Data.csv contains 
data about written records. All data in csv files are encrypted using 
the AES-128 cipher.
This version of the code corresponds to version 1.0, so if some 
functionalities do not work correctly, I will work on removing them.
Structure of data in User.csv:
               userID[0], username[1], password[2]
Structure of data in Data.csv:
      userID[0], dataID[1], domain[2] username[3], password[4]

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

from libraries.GUI import logIn, signIn, manager, addNew, showPassword, edit, delete
from libraries.cypher import encryption, decryption
from setup import initSetup
import libraries.csvLib as csv
import libraries.osLib as os

def main():
    if (os.path.exists("database") == False):
        initSetup()

    currentUserID = None
    flag = False

    while True:
        while True:
            var = logIn(error = flag)

            if ((var[0] == "") or (var[1] == "")):
                flag = True

            elif (((var[0] != "") or (var[1] != "")) and (var != "new_account")):
                flag = True
                with open('database/users.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if (var[0] == decryption(eval(row[1]))) and (var[1] == decryption(eval(row[2]))):
                            flag = False
                            currentUserID = decryption(eval(row[0]))
                            break
                if flag == False:
                    break
            
            elif (var == "new_account"):
                flag = False
                while True:
                    var = signIn(error = flag)

                    if ((var[0] == "") or (var[1] == "")):
                        flag = True

                    elif ((var[0] != "") or (var[1] != "")):
                        flag = False
                        with open('database/users.csv', 'r') as file:
                            reader = csv.reader(file)
                            for row in reader:
                                if decryption(eval(row[1])) == var[0]:
                                    flag = True
                                    break
                    
                    if (flag == False):
                        with open('database/users.csv', 'r') as file:
                            reader = csv.reader(file)
                            t = []
                            for row in reader:   
                                t.append(row)
                            if (len(t) == 0):
                                newUserID = 1
                            else:
                                newUserID = int(decryption(eval(t[len(t) - 1][0]))) + 1
                            t.append([encryption(str(newUserID)), encryption(var[0]), encryption(var[1])])
                        with open('database/users.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(t)
                        break

        while True:
            dataCurrentUser = []
            with open('database/data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if decryption(eval(row[0])) == currentUserID:
                        dataCurrentUser.append([decryption(eval(row[0])), decryption(eval(row[1])), decryption(eval(row[2])), decryption(eval(row[3])), decryption(eval(row[4]))])

            var = manager(dataCurrentUser)

            if (var == "logOut"):
                break
            
            elif (var == "create"):
                flag = False
                while True:
                    var = addNew(error = flag)

                    if (var == "back"):
                        break

                    elif ((var[0] == "") or (var[1] == "") or (var[2] == "")):
                        flag = True

                    elif (((var[0] != "") or (var[1] != "") or (var[2] != "")) and (var != "back")):
                        with open('database/data.csv', 'r') as file:
                            reader = csv.reader(file)
                            t = []
                            for row in reader:
                                t.append(row)
                            if (len(t) == 0):
                                dataID = 1
                            else:
                                dataID = int(decryption(eval(t[len(t) - 1][1]))) + 1
                            t.append([encryption(currentUserID), encryption(str(dataID)), encryption(var[0]), encryption(var[1]), encryption(var[2])])
                        with open('database/data.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(t)
                        break
            
            elif (var[0] == "edit"):
                with open('database/data.csv', 'r') as file:
                    reader = csv.reader(file)
                    t = []
                    for row in reader:
                        if (decryption(eval(row[1])) == var[1]):
                            var = edit([decryption(eval(row[0])), decryption(eval(row[1])), decryption(eval(row[2])), decryption(eval(row[3])), decryption(eval(row[4]))])
                            if var == "pass":
                                t.append(row)
                            else:
                                t.append([row[0], row[1], encryption(var[0]), encryption(var[1]), encryption(var[2])])
                        else:
                            t.append(row)
                with open('database/data.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(t)

            elif (var[0] == "show"):
                with open('database/data.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if (decryption(eval(row[1])) == var[1]):
                            showPassword([decryption(eval(row[0])), decryption(eval(row[1])), decryption(eval(row[2])), decryption(eval(row[3])), decryption(eval(row[4]))])
                            break

            elif var[0] == "del":
                with open('database/data.csv', 'r') as file:
                    reader = csv.reader(file)
                    t = []
                    for row in reader:
                        if (decryption(eval(row[1])) == var[1]):
                            var = delete([decryption(eval(row[0])), decryption(eval(row[1])), decryption(eval(row[2])), decryption(eval(row[3])), decryption(eval(row[4]))])
                            if var == "pass":
                                t.append(row)
                            else:
                                pass
                        else:
                            t.append(row)
                with open('database/data.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(t)

main()