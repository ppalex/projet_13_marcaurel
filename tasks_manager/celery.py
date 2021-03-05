from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('tasks_manager')

app.config_from_object('django.conf:settings', namespace="CELERY")


app.conf.beat_schedule = {
    'alert': {
        'task': 'tasks_manager.tasks.update_match_status',
        'schedule': crontab()
    }
}

app.autodiscover_tasks()
