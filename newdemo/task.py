from celery.registry import tasks
from celery.task import Task



class SignupTask(Task):
    def run(self,user):
        return "manikandan"


tasks.register(SignupTask)