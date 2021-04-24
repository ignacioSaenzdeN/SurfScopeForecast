from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from fantasyleague.api import fantasyleagueApi


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fantasyleagueApi.updateFantasyLeague,
                      'interval', minutes=43800)
    scheduler.start()
