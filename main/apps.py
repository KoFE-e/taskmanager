from django.apps import AppConfig  # библиотека для настройки веб-приложения


class MainConfig(AppConfig):  # класс настройки приложения
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'  # задаем название основного приложения
