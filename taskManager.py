import datetime as dt
import uuid
import os 
## class Job : ประกอบด้วย user_name, jobID, deadline


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()


class Job():
    def __init__(self,name, describe ,deadline ,job_id = str(uuid.uuid4().int)[:4]):
        self.name = name
        self.describe = describe
        self.deadline = deadline
        self.job_id = job_id
        pass
    def create_job(self):
        job_list.append({
        "name": self.name,
        "describe": self.describe,
        "deadline": self.deadline,
        "job_id": self.job_id
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

#-------1. start Program
job_list = [{"name": "backup Server", "describe": "ทำการ....", "deadline": "2025-01-2025", "job_id" : 4456},
            {"name": "checkSystem", "describe": "ทำการ....", "deadline": "2025-08-2026", "job_id" : 1240}
            ]

print("------------------------ Task Manager ------------------------")
display_list()
print("------------------------1. Add Task --------------------------")
print("-----------------------2. Delete Task ------------------------")
menu_selector = int(input("Please Select a menu: "))
if menu_selector == 1:
    print("you selected")
    job_name = str(input("Please insert your job name :"))
    job_describe = str(input("Please describe your job :"))
    date_string = input("Enter a date in YYYY-MM-DD format: ")
    try:
        year, month, day = map(int, date_string.split('-'))
        user_date = dt.date(year, month, day)
        print(f"You entered: {user_date}")
    
        
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

    job = Job(job_name, job_describe, user_date)
    job.create_job()
    clear_terminal()
    display_list()
    
elif menu_selector == 2:
    job_id_to_remove = int(input("Please enter your job ID: "))
    job_list = [i for i in job_list if i['job_id'] != job_id_to_remove]
    clear_terminal()
    display_list()
  


else :
    print("...")
