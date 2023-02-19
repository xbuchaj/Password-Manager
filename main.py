from GUI import logIn, signIn, manager, addNew, showPassword, edit, delete
from cypher import encryption, decryption
import csv

def main():
    currentUserID = None
    flag = False

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

main()