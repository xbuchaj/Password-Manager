from GUI import logIn, signIn
import csv

def main():
    # Log in or sign in section
    flag = False
    while True:
        var = logIn(error=flag)

        # If user don't fill in whole form
        if (var[0] == "") or (var[1] == ""):
            flag = True

        # If user fill in whole form
        if (var[0] != "") or (var[1] != ""):
            with open('users.csv', 'r') as file:
                reader = csv.reader(file)
                flag = True
                for row in reader:
                    if (var[0] == row[0]) and (var[1] == row[1]):
                        flag = False
                        break
            if flag == False:
                break

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
                            t.append([var[0], var[1]])
                        with open('users.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(t)
                    if flag == False:
                        break
main()