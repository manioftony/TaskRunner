import datetime
import celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(run_every=(crontab(minute='*/2')), name="some_task", ignore_result=True)
def myTaskAnother():
    print ('This is another')


@celery.decorators.periodic_task(run_every=datetime.timedelta(seconds=5)) # here we assume we want it to be run every 5 mins
def myTask():
    print ('This wasn\'t so difficult')


##################### This will turn basic function into the celery task ##############
from celery.decorators import task
@task(name="sum_two_numbers")
def addvalues(x, y):
    return x + y

