from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import MessageListView, MessageDeleteView, MessageDetailView, MessageCreateView, MessageUpdateView, \
    ContactsTemplateView

# Присваиваем переменной название приложения автоматически из системных файлов фреймворка Django
app_name = MainConfig.name

# Прописываем к функциям  и их наменования
# Пример path('create/', MessageCreateView.as_view(), name='create'),
# первой переменной в скобках указываем по какому пути страница будет отображаться на сайте (http://127.0.0.1:8000/create/)
# второй переменной указываем на метод класса, который мы написали в view.py, в данном случае это класс создания объектов модели Product
# третьей переменной указываем наименование url путя, можно задать любое, чтобы потом к нему обращаться

urlpatterns = [
    path('', MessageListView.as_view(), name='list'),
    path('create/', MessageCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='delete'),
    path('product/<int:pk>/', cache_page(60)(MessageDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', MessageUpdateView.as_view(), name='edit'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
]
