import uuid

from django.db import models
from django.urls import reverse


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, verbose_name='Название теста')
    worktime = models.IntegerField(verbose_name='Время выполнения (мин)')
    questionscount = models.IntegerField(verbose_name='Количество вопросов')
    statisfactorily = models.IntegerField(verbose_name='Удовлетворительно')
    good = models.IntegerField(verbose_name='Хорошо')
    perfect = models.IntegerField(verbose_name='Отлично')

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': str(self.pk)})

class Question(models.Model):
    profileid = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    text = models.TextField(verbose_name='Текст вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Answer(models.Model):
    questionid = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    isright = models.BooleanField()

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text


class Result(models.Model):
    profileid = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    username = models.CharField(max_length=300, verbose_name="ФИО")
    datetime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время завершения")
    rating = models.FloatField(verbose_name="Проценты")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
