from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_popular_feed_updater, 'interval', hours=1)
    scheduler.add_job(schedule_following_feed_updater, 'interval', minutes=1)
    scheduler.start()
