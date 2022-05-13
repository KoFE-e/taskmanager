from django.contrib import admin  # импортируем панель администратора сайта
from .models import Task  # импортируем модель задачи из файла models.py


admin.site.register(Task)  # регестрируем модель Task для возможности добавления и изменения через панель администратора
