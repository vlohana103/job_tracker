


welcome = "Welcome to the Job Application Tracker"
print("*" * len(welcome))
print(welcome)
print("*" * len(welcome))
print()


while True:
    print("*** Main Menu ***")
    enter = input("Press Y to begin or N to exit\n").lower()

    if enter == "y":
        pass
    elif enter == "n":
        print("Exiting the Job Application Tracker...")
        break
    else:
        print("Invalid Input. Please enter Y or N\n")