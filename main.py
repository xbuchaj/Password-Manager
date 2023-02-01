from GUI import logIn, signIn, manager, addNew, showPassword, edit
import csv

def main():
    # While because when user want to log out
    while True:

        # Variable for current user id
        userID = None

        # Log in or sign in section
        flag = False
        while True:
            var = logIn(error=flag)

            # If user don't fill in whole form
            if (var[0] == "") or (var[1] == ""):
                flag = True

            # If user select option to create new account
            elif var == "new_account":
                flag = False
                while True:
                    var = signIn(error = flag)

                    # If user don't fill in whole form
                    if (var[0] == "") or (var[1] == ""):
                        flag = True

                    # If user fill in whole form
                    else:

                        # Check if user write username which already exist
                        with open('users.csv', 'r') as file:
                            reader = csv.reader(file)
                            for row in reader:
                                if row[0] == var[0]:
                                    flag = True
                                    break
                                flag = False
                        
                        # If user didn't write username which already exist
                        if flag != True:
                            with open('users.csv', 'r') as file:
                                reader = csv.reader(file)
                                t = []
                                for row in reader:
                                    t.append(row)
                                if t[len(t) - 1][2] == "UserID":
                                    id = 1
                                else:
                                    id = int(t[len(t) - 1][2]) + 1
                                t.append([var[0], var[1], id])
                            with open('users.csv', 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(t)
                        if flag == False:       
                            break

            # If user fill in whole form
            else:
                with open('users.csv', 'r') as file:
                    reader = csv.reader(file)
                    flag = True
                    for row in reader:
                        if (var[0] == row[0]) and (var[1] == row[1]):
                            flag = False
                            userID = row[2]
                            break
                if flag == False:
                    break
        
        # Run main menu of manager
        while True:

            # Load data from database for current user
            userData = []
            with open('data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == userID:
                        userData.append(row)

            var = manager(userData)

            # If user want to log out
            if var == "logOut":
                break

            # If user want to create new record
            elif var == "create":
                flag = False
                while True:
                    var = addNew(error = flag)

                    # If user want to go back to main menu
                    if var == "back":
                        break

                    # If user don't fill in whole form
                    elif (var[0] == "") or (var[1] == "") or (var[2] == ""):
                        flag = True

                    # If user fill in whole form
                    else:
                        flag = False
                        with open('data.csv', 'r') as file:
                            reader = csv.reader(file)
                            t = []
                            for row in reader:
                                t.append(row)
                            if t[len(t) - 1][1] == "DomainID":
                                id = 1
                            else:
                                id = int(t[len(t) - 1][1]) + 1
                            t.append([userID, id, var[0], var[1], var[2]])  
                        with open('data.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(t)

                    if flag == False:
                        break

            # If user want to edit record
            elif var[0] == "edit":
                with open('data.csv', 'r') as file:
                    reader = csv.reader(file)
                    t = []
                    for row in reader:
                        if row[1] == var[1]:
                            var = edit(row)
                            t.append([row[0], row[1], var[0], var[1], var[2]])
                        else:
                            t.append(row)
                with open('data.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(t)

            # If user want to see the passford of record
            elif var[0] == "show":
                with open('data.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[1] == var[1]:
                            showPassword(row)
                            break

            # If user want to delete record
            #elif var[0] == "del":

        # If user want to log out
        continue

main()