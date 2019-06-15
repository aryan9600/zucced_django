from django.apps import AppConfig

class AuthenticationAppConfig(AppConfig):
    name = 'authenticaiton'
    label = 'authentication'
    verbose = 'Authentication'

    def ready(self):
        import authentication.signals

default_app_config = 'AuthenticationAppConfig'