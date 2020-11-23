from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print('==============Starting Clock Script=================')
    exec(open("getovkino.py").read())

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(job_function, 'interval', hours=20)

sched.start()
