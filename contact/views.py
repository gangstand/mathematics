from django.views.generic import CreateView
from .models import Contact
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin


class ContactCreate(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm
    success_message = 'Письмо отправлено'

    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение с формы от {data["first_name"]} {data["last_name"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


def email(subject, content):
    send_mail(subject, content, 'ganggstand@gmail.com', ['kulpinikita@gmail.com'])
