from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))  # чтобы не перечислять пути дважды, передаем наш файл с ссылками из приложения main
]
