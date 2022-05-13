from django.urls import path
from . import views  # импортируем файл views.py

urlpatterns = [  # шаблоны для путей сайта, ссылки
    path('', views.index, name='home'),  # ссылка на главную страницу сайта
    path('create', views.create, name='create'),  # ссылка на страницу создания задачи
    path('delete/<int:id>/', views.delete),  # ссылка на кнопку удаления задачи
]
