from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=55)
def timed_job():
    print('Starting Clock Script')
    exec(open("getovkino.py").read())


#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
#def scheduled_job():
#    print('This job is run every weekday at 5pm.')
    
    
sched.start()
