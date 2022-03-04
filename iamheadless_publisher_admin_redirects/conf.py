from .apps import IamheadlessPublisherAdminRedirectsConfig


class Settings:

    APP_NAME = IamheadlessPublisherAdminRedirectsConfig.name
    ITEM_TYPE = 'redirect'

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
