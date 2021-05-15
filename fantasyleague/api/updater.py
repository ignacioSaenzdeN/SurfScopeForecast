from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from fantasyleague.api import fantasyleagueApi

# start() calls updateFantasyLeague in fantasyleagueAPI
# every month to update the results of the user


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fantasyleagueApi.updateFantasyLeague,
                      'interval', minutes=43800)
    scheduler.start()
