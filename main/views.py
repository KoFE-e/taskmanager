from django.shortcuts import render, redirect  # подключаем функцию render для отображения страницы по ссылке, redirect - для переадресации
from .models import Task  # импортируем модель задачи из файла models.py
from .forms import TaskForm  # импортируем форму для задачи из файла forms.py


def index(request):  # функция для отображения главной страницы
    tasks = Task.objects.order_by('-id')  # берем задачи из модели Task в порядке, обратном времени добавления
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})  # отображаем главную страницу


def create(request):  # функция для отображения страницы создания сайта
    error = ''
    if request.method == 'POST':  # если пользователь нажал кнопку для отправки формы
        form = TaskForm(request.POST)  # получаем данные из этой формы
        if form.is_valid():  # если она корректна, то сохраняем ее и возвращаемся на главную страницу
            form.save()
            return redirect('home')
        else:  # иначе выводим ошибку
            error = 'Форма некорректна'

    form = TaskForm()  # создаем новую форму
    context = {  # контекст для вывода формы и ошибки
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)  # отображаем страницу создания задачи с учетом контекста


def delete(request, id):  # функция для удаления записи из БД
    try:
        tasks = Task.objects.get(id=id)  # получаем ID записи, которую пользователь хочет удалить
        tasks.delete()  # удаляем запись
        return redirect('home')  # отображение главной страницы
    except:
        return redirect('home')
