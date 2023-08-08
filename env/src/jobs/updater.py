from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_feed_updater

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_feed_updater, 'interval', seconds=10)
    scheduler.start()
