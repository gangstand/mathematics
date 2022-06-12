from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class OneCourseVideo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема')
    body = models.TextField(verbose_name='Краткая информация')
    video = models.FileField(upload_to='ocv/', verbose_name='Видеофайл')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Видеоуроки 1 курс'
        verbose_name_plural = 'Видеоуроки 1 курс'


class TwoCourseVideo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема')
    body = models.TextField(verbose_name='Краткая информация')
    video = models.FileField(upload_to='otv/', verbose_name='Видеофайл')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Видеоуроки 2 курс'
        verbose_name_plural = 'Видеоуроки 2 курс'


class MetodicalOneCourses(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    file = models.FileField(upload_to='metodical/', verbose_name='Файл')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Методические указания 1 курса'
        verbose_name_plural = 'Методические указания 1 курса'


class MetodicalTwoCourses(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    file = models.FileField(upload_to='metodical/', verbose_name='Файл')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Методические указания 2 курса'
        verbose_name_plural = 'Методические указания 2 курса'
