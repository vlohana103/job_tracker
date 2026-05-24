import jobs

tracker = {}
# C.R.U.D

def create():
    if not tracker:
        id_count = 1
    else:
        id_count = max(tracker) + 1

    company_name = input("Company Name:\n")
    job_title = input("Job Title:\n")
    url = input("URL:\n")
    status = ""
    while status == "":
        ask_status = int(input("Status:\nEnter Status Option:\n1: No Update\n2: Interviewing\n3: Accepted\n4: Rejected\n"))
        if ask_status == 1:
            status = "NO UPDATE"
        elif ask_status == 2:
            status = "INTERVIEWING"
        elif ask_status == 3:
            status = "ACCEPTED"
        elif ask_status == 4:
            status = "REJECTED"
        else:
            print("Invalid Status Input!")
    date_applied = input("Date Applied:\n")
    last_updated = input("Date Updated:\n")

    tracker[id_count] = jobs.Job_Application(id_count, company_name, job_title, url, status, date_applied, last_updated)


def read():
    if len(tracker) == 0:
        print("\nTracker Log is empty")
        return

    for job in tracker.values():
        print(job.job_id, job.company_name, job.job_title, job.url, job.status, job.date_applied, job.last_updated)
        print("-" * 30)


def update():
    job_search = int(input("Enter the JOB ID you would like to update:\n"))
    if job_search in tracker:
        print(f"You are updating: {tracker[job_search].company_name}")

        print("What would you like to change?")
        choice = int(input("1. Update: Job Title\n2. Update: Url\n3. Update: Status\n4. Update: Date Updated\n"))

        if choice == 1:
            new_Job_title = input("Enter Updated Job Title:\n")
            tracker[job_search].job_title = new_Job_title
            print(f"Job Title updated to {new_Job_title}")
        elif choice == 2:
            new_URL = input("Enter Updated URL\n")
            tracker[job_search].url = new_URL
            print(f"URL updated to {new_URL}")
        elif choice == 3:
            new_status = ""
            while new_status == "":
                ask_status = int(input("New Status:\nEnter New Status Option:\n1: No Update\n2: Interviewing\n3: Accepted\n4: Rejected\n"))
                if ask_status == 1:
                    new_status = "NO UPDATE"
                elif ask_status == 2:
                    new_status = "INTERVIEWING"
                elif ask_status == 3:
                    new_status = "ACCEPTED"
                elif ask_status == 4:
                    new_status = "REJECTED"
                else:
                    print("Invalid New Status Input!")

            tracker[job_search].status = new_status
            print(f"Status updated to {new_status}")
        elif choice == 4:
            new_Date = input("Enter Updated Date\n")
            tracker[job_search].last_updated = new_Date
            print(f"Last Updated field changed to {new_Date}")

    else:
        print("No log associated with that job ID\n")

def delete():
    job_delete = int(input("Enter the Job ID you want to DELETE:\n"))
    if job_delete in tracker:
        confirm = input(f"ARE YOU SURE YOU WANT TO DELETE THE JOB LOG: {job_delete}?\n type \"YES\" to confirm. Enter anything else to exit.")
        if confirm == "YES":
            del tracker[job_delete]
            print("Log has been deleted.")
        else:
            print("You've chosen to not delete any log.")
    else:
        print("No log associated with that job ID\n")



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
                print("*** Creating Job Log ***")
                create()
            # Read
            elif ask == "2":
                print("*** Reading Job Log ***")
                read()
            # Update
            elif ask == "3":
                print("*** Updating Job Log ***")
                update()
            # Delete
            elif ask == "4":
                print("*** Deleting Job Log ***")
                delete()
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