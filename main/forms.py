from .models import Task  # импортируем модель задачи из файла models.py
from django.forms import ModelForm, TextInput, Textarea  # библиотека ModelForm для создания формы, TextInput для ввода небольшого текста, Textarea для ввода большого текста


class TaskForm(ModelForm):  # класс для описания самой формы, по которой будут заноситься данные в БД
    class Meta:
        model = Task  # задаем модель для формы
        fields = ["title", "task"]  # задаем поля для формы
        widgets = {  # словарь для сопоставления полей формы и введенных пользователем данных
            "title": TextInput(attrs={
                'class': 'form-control',  # класс формы
                'placeholder': 'Введите название'  # что видит пользователь в поле, если еще ничего не введено
            }),
            "task": Textarea(attrs={
                'class': 'form-control',  # класс формы
                'placeholder': 'Введите описание'  # что видит пользователь в поле, если еще ничего не введено
            }),
        }