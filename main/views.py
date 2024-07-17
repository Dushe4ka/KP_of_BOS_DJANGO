from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView, TemplateView
from django.db.models import Q

from main.forms import MessageForm
from main.models import Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:list')

    def get_success_url(self):
        return reverse('main:view', args=[self.kwargs.get('pk')])


class MessageListView(ListView):
    model = Message
    template_name = 'main/message_list.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        if query:
            object_list = Message.objects.filter(
                Q(title__icontains=query))
            return object_list
        else:
            return Message.objects.all()


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('main:list')


class ContactsTemplateView(TemplateView):
    template_name = 'main/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"\n\nИмя - {name}\n"
              f"Телефон - {phone}\n"
              f"Сообщение - {message}\n\n")

        return super().get(request, *args, **kwargs)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"\n\nИмя - {name}\n"
              f"Телефон - {phone}\n"
              f"Сообщение - {message}\n\n")

    return render(request, 'contacts.html')