from django.forms import ModelForm

from main.models import Message
"""
Здесь представлены формы моделей в которых :
- ProductForm представляет форму создания и редактирования продукта
- CategoryForm представляет форму создания и редактирования категории
в model = ... мы пишем название модели к которой пишем форму
fields = "__all__" указывает что все поля модели будут использоваться в форме, если они не указаны явно.
"""


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
