from django.db import models  # библиотека для работы с моделями для БД


class Task(models.Model):  # описание класса модели задач(имеют название и описание)
    title = models.CharField('Задача', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):  # функция для отображения названий задач на этапе отладки сайта
        return self.title

    class Meta:  # вспомогательный класс для отображения в правильных числах
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'