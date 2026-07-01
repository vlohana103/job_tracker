
import json
import jobs
 
DATA_FILE = "tracker.json"
 
tracker = {}
 
# ============== Persistence ==============
 
def save():
    data = [job.to_dict() for job in tracker.values()]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
 
def load():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        for entry in data:
            job = jobs.Job_Application.from_dict(entry)
            tracker[job.job_id] = job
    except FileNotFoundError:
        pass  # First run — no file yet, start with empty tracker
    except (json.JSONDecodeError, KeyError):
        print("Warning: tracker data file could not be read. Starting fresh.")
 
# ============== Status Helper ==============
 
STATUS_MAP = {
    "1": "NO UPDATE",
    "2": "INTERVIEWING",
    "3": "ACCEPTED",
    "4": "REJECTED"
}
 
STATUS_PROMPT = (
    "Enter Status Option:\n"
    " 1: No Update\n"
    " 2: Interviewing\n"
    " 3: Accepted\n"
    " 4: Rejected\n"
)
 
def get_status():
    while True:
        choice = input(STATUS_PROMPT).strip()
        if choice in STATUS_MAP:
            return STATUS_MAP[choice]
        print("Invalid option. Please enter 1, 2, 3, or 4.")
 
# ============== C.R.U.D ==============
 
def create():
    job_id = 1 if not tracker else max(tracker) + 1
 
    company_name = input("Company Name:\n").strip()
    job_title = input("Job Title:\n").strip()
    url = input("URL:\n").strip()
    status = get_status()
    date_applied = input("Date Applied:\n").strip()
    last_updated = input("Date Last Updated:\n").strip()
 
    tracker[job_id] = jobs.Job_Application(
        job_id, company_name, job_title, url, status, date_applied, last_updated
    )
    save()
    print(f"\nJob log #{job_id} created for {company_name}.\n")
 
 
def read():
    if not tracker:
        print("\nTracker log is empty.\n")
        return
 
    print()
    print("-" * 70)
    for job in tracker.values():
        print(f"ID:           {job.job_id}")
        print(f"Company:      {job.company_name}")
        print(f"Job Title:    {job.job_title}")
        print(f"URL:          {job.url}")
        print(f"Status:       {job.status}")
        print(f"Date Applied: {job.date_applied}")
        print(f"Last Updated: {job.last_updated}")
        print("-" * 70)
    print()
 
 
def update():
    try:
        job_id = int(input("Enter the Job ID you would like to update:\n"))
    except ValueError:
        print("Please enter a valid numeric ID.\n")
        return
 
    if job_id not in tracker:
        print("No log associated with that Job ID.\n")
        return
 
    job = tracker[job_id]
    print(f"Updating: {job.company_name} — {job.job_title}")
 
    try:
        choice = int(input(
            "What would you like to change?\n"
            " 1. Job Title\n"
            " 2. URL\n"
            " 3. Status\n"
            " 4. Date Last Updated\n"
        ))
    except ValueError:
        print("Please enter a number.\n")
        return
 
    if choice == 1:
        job.job_title = input("Enter updated Job Title:\n").strip()
        print(f"Job Title updated to: {job.job_title}")
    elif choice == 2:
        job.url = input("Enter updated URL:\n").strip()
        print(f"URL updated to: {job.url}")
    elif choice == 3:
        job.status = get_status()
        print(f"Status updated to: {job.status}")
    elif choice == 4:
        job.last_updated = input("Enter updated date:\n").strip()
        print(f"Last Updated set to: {job.last_updated}")
    else:
        print("Invalid option.\n")
        return
 
    save()
    print()
 
 
def delete():
    try:
        job_id = int(input("Enter the Job ID you want to DELETE:\n"))
    except ValueError:
        print("Please enter a valid numeric ID.\n")
        return
 
    if job_id not in tracker:
        print("No log associated with that Job ID.\n")
        return
 
    confirm = input(
        f"Are you sure you want to delete log #{job_id} "
        f"({tracker[job_id].company_name})? Type YES to confirm:\n"
    )
    if confirm == "YES":
        del tracker[job_id]
        save()
        print("Log deleted.\n")
    else:
        print("Delete cancelled.\n")
 
 
# ============== Core Logic ==============
 
load()
 
welcome = "Welcome to the Job Application Tracker"
print("*" * len(welcome))
print(welcome)
print("*" * len(welcome))
print()
 
while True:
    ask = input(
        "*** Main Menu ***\n"
        " 1. Add job log\n"
        " 2. View all logs\n"
        " 3. Update a log\n"
        " 4. Delete a log\n"
        " 5. Exit\n"
    ).strip()
 
    if ask == "1":
        print("*** Creating Job Log ***")
        create()
    elif ask == "2":
        print("*** Viewing Job Logs ***")
        read()
    elif ask == "3":
        print("*** Updating Job Log ***")
        update()
    elif ask == "4":
        print("*** Deleting Job Log ***")
        delete()
    elif ask == "5":
        print("Exiting Job Application Tracker. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 1–5.\n")


