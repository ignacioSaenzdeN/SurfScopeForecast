from django.apps import AppConfig


class FantasyleagueConfig(AppConfig):
    name = 'fantasyleague'

    def ready(self):
        #print("inside ready")
        from fantasyleague.api import updater
        updater.start()
