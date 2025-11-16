import datetime as dt
import uuid
## class Job : ประกอบด้วย user_name, jobID, deadline
print("------------------------ Task Manager ------------------------")
print("------------------------1. Add Task --------------------------")
print("----------------------- 2. Display Job -----------------------")
menu_selector = int(input("Please Select a menu: "))
job_list = [{"name": "backup Server", "describe": "ทำการ....", "deadline": "25-08-2025", "jobID" : 4456}]
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
    
    


else :
    print("...")




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
    def display_job(self):
        pass
    def save_job(self):
        pass
    def search_job(self):
        pass



job = Job(job_name, job_describe, user_date)
job.create_job()
print(f"{job.name}")
print(job_list)
    

