#!/usr/bin/python
from __future__ import print_function
from datetime import time, datetime, timedelta
from tasklib import Task, local_zone, TaskWarrior
from pytz import timezone, utc

# DEFAULT_TIME = time(22,0,0)  # Your wanted default time
conf = TaskWarrior().config

def get_conf_value(config, value, default, process=(lambda x: x)):
    if value in config:
        if isinstance(default, bool):
            if config[value].lower() in ['true', '1', 'yes']:
                return True
            else: return False
        else: return process(config[value])
    else: return default

default_time = get_conf_value(conf, 'default.time', 
        time(0,0,0), 
        (lambda t: datetime.strptime(t, u'%H:%M').time()))

def is_local_midnight(timestamp):
    return timestamp.astimezone(local_zone).time() == time(0,0,0)

def set_default_time(timestamp):
    return timestampastimezone(local_zone).replace(
        hour=default_time.hour,
        minute=default_time.minute,
        second=default_time.second,
        )

def hook_default_time(task):
    if task['due'] and is_local_midnight(task['due']):
        task['due'] = set_default_time(task['due'])
        print("Default due time has been set.")

if __name__ == '__main__':
    print(default_time)
