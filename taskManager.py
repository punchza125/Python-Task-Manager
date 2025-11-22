import datetime as dt
import uuid
import os 
import json
import time

## class Job : ประกอบด้วย user_name, jobID, deadline

state = True
job_list = [
    {"name": "backup Server", "describe": "ทำการ....", "deadline": "2025-01-15", "job_id": "4456", "status": "unfinished"},
    {"name": "checkSystem", "describe": "ทำการ....", "deadline": "2025-08-24", "job_id": "1240", "status": "unfinished"}
]

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



class Job():
    def __init__(self,name, describe ,deadline ,job_id = str(uuid.uuid4().int)[:4],job_status = "unfinished"):
        self.name = name
        self.describe = describe
        self.deadline = deadline
        self.job_id = job_id
        self.job_status = job_status
        pass
    def create_job(self):
        job_list.append({
        "name": self.name,
        "describe": self.describe,
        "deadline": self.deadline,
        "job_id": self.job_id,
        "status": self.job_status
    })

# แสดงผล
def display_list():
    # รวบรวม key ทั้งหมด
    headers = set()
    for i in job_list:
        headers.update(i.keys())

    # แปลงจาก set เป็น list และจัดลำดับให้ job_id อยู่หน้า
    headers = list(headers)

    # ถ้าต้องการให้ job_id อยู่ลำดับแรก
    if "job_id" in headers:
        headers.remove("job_id")
        headers.insert(0, "job_id")

    # คำนวณความกว้างแต่ละคอลัมน์
    widths = {}
    for h in headers:
        max_len = len(h)
        for i in job_list:
            max_len = max(max_len, len(str(i.get(h, ""))))
        widths[h] = max_len

    # print header
    header_row = " | ".join(h.ljust(widths[h]) for h in headers)
    print(header_row)
    print("-" * len(header_row))

    # print each row
    for i in job_list:
        row = " | ".join(str(i.get(h, "")).ljust(widths[h]) for h in headers)
        print(row)
    
def search_jobs(jobs, keyword=None, enddate=None):
    results = jobs

    if keyword: 
        keyword_lower = keyword.lower()
        results = [
            job for job in results
            if keyword_lower in job['name'].lower() or keyword_lower in job['describe'].lower()
        ]

    if enddate:
        results = [
            job for job in results
            if job['deadline'] == enddate
        ]

    return results
while state == True:
    clear_terminal()
    #-------1. start Program

    print("------------------------ Task Manager ------------------------")
    display_list()
    print("1. Add Task ")
    print("2. Delete Task")
    print("3. Search Task")
    print("4. Change status")
    print("5. Save")
    print("6. Load")
    print("99. Exit")
    menu_selector = int(input("Please Select a menu: "))
    if menu_selector == 1:
        print("you selected")
        while True:
            job_name = str(input("Please insert your job name :"))
            if job_name:
                print(f"You entered: {job_name}")
                break
            else:
                print("Input cannot be empty. Please try again.")
        
        job_describe = str(input("Please describe your job :"))
        while True:
            date_string = input("Enter a date in YYYY-MM-DD format: ")

            try:
                year, month, day = map(int, date_string.split('-'))
                user_date = dt.date(year, month, day)
                break
        
            
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        job = Job(job_name, job_describe, str(user_date))
        job.create_job()
        clear_terminal()
        # display_list()
        
    elif menu_selector == 2:
        job_id_to_remove = input("Please enter your job ID: ")
        job_list = [i for i in job_list if i['job_id'] != job_id_to_remove]

        clear_terminal()
        display_list()



    elif menu_selector == 3:
        print("1. Search by keyword")
        print("2. Search by deadline")
        search_choice = int(input("Please select choice 1-2 : "))

        if search_choice == 1:
            search_key = input("Please input your keyword: ")
            found_jobs = search_jobs(job_list, keyword=search_key)


        elif search_choice == 2:
            search_deadline = input("Please input your deadline: ")
            found_jobs = search_jobs(job_list, enddate=search_deadline)


        else:
            print("Wrong input!!")
            found_jobs = []
        clear_terminal()
        print(f"\nพบงานทั้งหมด {len(found_jobs)} รายการ:")
        for job in found_jobs:
            print(job)

            print("1. Go back to menu")
            print("2. Exit")
            search_end_choice = int(input("Please select your choice:"))
            if search_end_choice == 1:
                pass
            else:
                state = False
    elif menu_selector == 4:
        job_id_to_change = input("Enter job ID to change status: ")

        found = False
        for job in job_list:
            if job["job_id"] == job_id_to_change:
                found = True
                # toggle
                if job["status"] == "unfinished":
                    job["status"] = "finished"
                    print(f"Status changed: unfinished → finished")
                else:
                    job["status"] = "unfinished"
                    print(f"Status changed: finished → unfinished")
                break

        if not found:
            print("Job ID not found!")

        time.sleep(2)

    elif menu_selector == 5:
        with open('data.json', 'w') as f:
            json.dump(job_list, f, indent = 4)
        print("Saving...")
        time.sleep(3)
    elif menu_selector == 6:
        with open('data.json', 'r') as f:
            job_list = json.load(f)
        print("Loading...")
        time.sleep(3)



        

    elif menu_selector == 99:
        state = False
        
    else :
        print("...")

