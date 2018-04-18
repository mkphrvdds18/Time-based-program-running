
# code tested on anaconda win 7 win 10, basic package did not have schedule, pls install using below command
# pip install schedule
# to stop the job, press ctrl+c from keyboard

import schedule
import time

from datetime import datetime

time_now = datetime.now()

def job():
  print("I will do a print job for now ..and each interval..")
  print("you can run anything - like checking some dynamic content")
  print("Current time: ", time_now)

# run the job 1st time then start after the interval

job()
schedule.every(1).minutes.do(job)

'''
# these are very good example 

schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).days.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

'''


while True:
    schedule.run_pending()
    time.sleep(1)
