from django.conf import settings as dj_settings

from .apps import IamheadlessPublisherAdminRedirectsConfig as AppConfig


class Settings:

    APP_NAME = AppConfig.name
    ITEM_TYPE = 'redirect'

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
