from GUI import logIn, signIn, manager, addNew, showPassword, edit, delete
from cypher import encryption, decryption
import csv

def main():
    currentUserID = None
    flag = False

    while True:
        while True:
            var = logIn(error = flag)

            if ((var[0] == "") or (var[1] == "")):
                flag = True

            elif (((var[0] != "") or (var[1] != "")) and (var != "new_account")):
                flag = True
                with open('users.csv', 'r') as file:
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
                        with open('users.csv', 'r') as file:
                            reader = csv.reader(file)
                            for row in reader:
                                if decryption(eval(row[1])) == var[0]:
                                    flag = True
                                    break
                    
                    if (flag == False):
                        with open('users.csv', 'r') as file:
                            reader = csv.reader(file)
                            t = []
                            for row in reader:   
                                t.append(row)
                            if (len(t) == 0):
                                newUserID = 1
                            else:
                                newUserID = int(decryption(eval(t[len(t) - 1][0]))) + 1
                            t.append([encryption(str(newUserID)), encryption(var[0]), encryption(var[1])])
                        with open('users.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(t)
                        break

        while True:
            dataCurrentUser = []
            with open('data.csv', 'r') as file:
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
                        with open('data.csv', 'r') as file:
                            reader = csv.reader(file)
                            t = []
                            for row in reader:
                                t.append(row)
                            if (len(t) == 0):
                                dataID = 1
                            else:
                                dataID = int(decryption(eval(t[len(t) - 1][1]))) + 1
                            t.append([encryption(currentUserID), encryption(str(dataID)), encryption(var[0]), encryption(var[1]), encryption(var[2])])
                        with open('data.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(t)
                        break
            
            elif (var[0] == "edit"):
                with open('data.csv', 'r') as file:
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
                with open('data.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(t)

            elif (var[0] == "show"):
                with open('data.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if (decryption(eval(row[1])) == var[1]):
                            showPassword([decryption(eval(row[0])), decryption(eval(row[1])), decryption(eval(row[2])), decryption(eval(row[3])), decryption(eval(row[4]))])
                            break

            elif var[0] == "del":
                with open('data.csv', 'r') as file:
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
                with open('data.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(t)

main()