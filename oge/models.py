from django.db import models


class VariantOge(models.Model):
    title_oge = models.CharField(max_length=255, verbose_name='Номер варианта')
    file_oge = models.FileField(upload_to='ege/', verbose_name='Файл варианта')

    def __str__(self):
        return self.title_oge

    class Meta:
        verbose_name = 'Вариант ОГЭ'
        verbose_name_plural = 'Варианты ОГЭ'


class BlockAlgebraOge(models.Model):
    title_algebra_oge = models.CharField(max_length=255, verbose_name='Название блока')
    file_algebra_oge = models.FileField(upload_to='algebra/', verbose_name='Файл блока')

    def __str__(self):
        return self.title_algebra_oge

    class Meta:
        verbose_name = 'Программа блока Алгебра ОГЭ'
        verbose_name_plural = 'Программы блоков Алгебра ОГЭ'


class BlockGeometriaOge(models.Model):
    title_geometria_oge = models.CharField(max_length=255, verbose_name='Название блока')
    file_geometria_oge = models.FileField(upload_to='geometria/', verbose_name='Файл блока')

    def __str__(self):
        return self.title_geometria_oge

    class Meta:
        verbose_name = 'Программа блока Геометрия ОГЭ'
        verbose_name_plural = 'Программы блоков Геометрия ОГЭ'
