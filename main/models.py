from django.db import models


# Create your models here.
class Cert(models.Model):
    title_cert = models.CharField(max_length=255, verbose_name='Название сертификата')
    file_cert = models.FileField(upload_to='cert/', verbose_name='Файл сертификата')

    def __str__(self):
        return self.title_cert

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
