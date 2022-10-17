from django_cron import CronJobBase, Schedule
from .models import Deleted
import json


class DeletedClearCron(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'core.DeletedClearCron'

    def do(self):
        with open('data.txt', 'w') as outfile:
            json.dumps({'human': 'asdasdasda'}, outfile)
