
# Show options menu

def show_menu():
    action=0
    while True:
        try:
            action=int(input(
                    "(1) Add student details""\n"
                    "(2) See the added students""\n"
                    "(3) See the top 3 students based on their average grade""\n"
                    "(4) Import student details""\n"
                    "(5) Export the student details""\n"
                    "(6) See Global average of all students""\n"
                    "(7) Exit""\n"
                    "\n""Choose one of the options by typing its corresponding option number:"))
            if action >7 or action <1:
                print("\n"" ** The option does not exist, please try again! **""\n")
            else:
                break
        except ValueError:
            print("\n""** This is not a valid number, please try again! **""\n")
    return action