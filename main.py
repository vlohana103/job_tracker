import jobs

# C.R.U.D
tracker = {}

def create():
    pass

def read():
    pass

def update():
    pass

def delete():
    pass


# ============== Core Logic ==============

welcome = "Welcome to the Job Application Tracker"
print("*" * len(welcome))
print(welcome)
print("*" * len(welcome))
print()

while True:
    print("*** Main Menu ***")
    enter = input("Press Y to begin or N to exit\n").lower()

    if enter == "y":
        while True:
            print("*** Using Job Application Tracker ***")
            ask = input("Press:\n 1 to Add\n 2 to View\n 3 to Update\n 4 to Delete\n 5 to Return to the Main Menu?\n")
            #C.R.U.D
            if ask == "1":
                pass
            # Create
            elif ask == "2":
                pass
            # Read
            elif ask == "3":
                pass
            # Update
            elif ask == "4":
                pass
            # Delete
            elif ask == "5":
                print("Returning to Main Menu...\n")
                break
            else:
                print("Invalid Input... \n")

    elif enter == "n":
        print("Exiting the Job Application Tracker...")
        break
    else:
        print("Invalid Input. Please enter Y or N\n")