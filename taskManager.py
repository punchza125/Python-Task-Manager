import datetime as dt
import uuid
import os 
import json
import time

# ---------------------- Global State ----------------------
state = True
DATA_FILE = "data.json"

job_list = [
    {"name": "backup Server", "describe": "ทำการ....", "deadline": "2025-01-15", "job_id": "4456", "status": "unfinished"},
    {"name": "checkSystem", "describe": "ทำการ....", "deadline": "2025-08-24", "job_id": "1240", "status": "unfinished"}
]


# ---------------------- Utility Function ----------------------
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_non_empty(prompt):
    """รับ input และบังคับให้ไม่เป็นค่าว่าง"""
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("Input cannot be empty. Please try again.")


def input_date(prompt):
    """รับวันที่รูปแบบ YYYY-MM-DD"""
    while True:
        date_string = input(prompt)
        try:
            year, month, day = map(int, date_string.split('-'))
            date_obj = dt.date(year, month, day)
            return str(date_obj)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


# ---------------------- Job Class ----------------------
class Job:
    def __init__(self, name, describe, deadline, job_id=None, status="unfinished"):
        self.name = name
        self.describe = describe
        self.deadline = deadline
        self.job_id = job_id or str(uuid.uuid4().int)[:4]
        self.status = status

    def to_dict(self):
        return {
            "name": self.name,
            "describe": self.describe,
            "deadline": self.deadline,
            "job_id": self.job_id,
            "status": self.status
        }

    def save(self):
        job_list.append(self.to_dict())


# ---------------------- Display ----------------------
def display_list():
    if not job_list:
        print("No tasks available.\n")
        return
    
    headers = ["job_id"] + sorted(h for h in job_list[0].keys() if h != "job_id")

    widths = {
        h: max(len(h), max(len(str(job.get(h, ""))) for job in job_list))
        for h in headers
    }

    header_row = " | ".join(h.ljust(widths[h]) for h in headers)
    print(header_row)
    print("-" * len(header_row))

    for job in job_list:
        row = " | ".join(str(job.get(h, "")).ljust(widths[h]) for h in headers)
        print(row)


# ---------------------- Search ----------------------
def search_jobs(keyword=None, enddate=None):
    results = job_list

    if keyword:
        keyword = keyword.lower()
        results = [job for job in results if
                   keyword in job['name'].lower() or keyword in job['describe'].lower()]

    if enddate:
        results = [job for job in results if job['deadline'] == enddate]

    return results


# ---------------------- File Operations ----------------------
def save_to_file():
    with open(DATA_FILE, 'w') as f:
        json.dump(job_list, f, indent=4)
    print("Saving...")
    time.sleep(1)


def load_from_file():
    global job_list
    if not os.path.exists(DATA_FILE):
        print("File not found!")
        return

    with open(DATA_FILE, 'r') as f:
        job_list = json.load(f)
    print("Loading...")
    time.sleep(1)


# ---------------------- Main Loop ----------------------
while state:
    clear_terminal()

    print("------------------------ Task Manager ------------------------")
    display_list()

    print("\n1. Add Task")
    print("2. Delete Task")
    print("3. Search Task")
    print("4. Change status")
    print("5. Save")
    print("6. Load")
    print("99. Exit")

    try:
        menu = int(input("Please select a menu: "))
    except ValueError:
        print("Invalid input!")
        time.sleep(1)
        continue

    # ADD
    if menu == 1:
        name = input_non_empty("Please enter job name: ")
        desc = input("Describe your job: ")
        deadline = input_date("Enter deadline (YYYY-MM-DD): ")

        job = Job(name, desc, deadline)
        job.save()

    # DELETE
    elif menu == 2:
        job_id = input("Enter job ID to delete: ")
        job_list = [job for job in job_list if job["job_id"] != job_id]

    # SEARCH
    elif menu == 3:
        print("1. Search by keyword")
        print("2. Search by deadline")

        try:
            choice = int(input("Choose 1-2: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            key = input("Enter keyword: ")
            results = search_jobs(keyword=key)

        elif choice == 2:
            date = input_date("Enter deadline (YYYY-MM-DD): ")
            results = search_jobs(enddate=date)

        else:
            print("Invalid choice!")
            continue

        clear_terminal()
        print(f"Found {len(results)} task(s):\n")
        for job in results:
            print(job)

        input("\nPress Enter to return to menu...")

    # CHANGE STATUS
    elif menu == 4:
        job_id = input("Enter job ID to toggle status: ")
        found = False

        for job in job_list:
            if job["job_id"] == job_id:
                job["status"] = "finished" if job["status"] == "unfinished" else "unfinished"
                found = True
                print("Status updated!")
                break

        if not found:
            print("Job not found!")

        time.sleep(1)

    elif menu == 5:
        save_to_file()

    elif menu == 6:
        load_from_file()

    elif menu == 99:
        state = False

    else:
        print("Invalid menu!")
        time.sleep(1)
