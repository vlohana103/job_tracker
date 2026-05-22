import jobs

# C.R.U.D
tracker = {}

def create():
    id_count = len(tracker) + 1

    company_name = input("Company Name:\n")
    job_title = input("Job Title:\n")
    url = input("URL:\n")
    status = input("Status:\n")
    date_applied = input("Date Applied:") # use Pythons built in system clock for this
    last_updated = input("Date Updated:\n")

    tracker[id_count] = jobs.Job_Application(id_count, company_name, job_title, url, status, date_applied, last_updated)


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
            # C.R.U.D
            # Create
            if ask == "1":
                create()
            # Read
            elif ask == "2":
                read()
            # Update
            elif ask == "3":
                pass
            # Delete
            elif ask == "4":
                pass
            # Return to Main Menu
            elif ask == "5":
                print("Returning to Main Menu...\n")
                break
            # Invalid Input
            else:
                print("Invalid Input... \n")

    elif enter == "n":
        print("Exiting the Job Application Tracker...")
        break
    else:
        print("Invalid Input. Please enter Y or N\n")