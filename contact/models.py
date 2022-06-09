from django.db import models
from django.urls import reverse


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    group = models.CharField(max_length=6)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('contact')
