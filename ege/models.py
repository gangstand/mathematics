from django.db import models


class VariantEge(models.Model):
    title_ege = models.CharField(max_length=255, verbose_name='Номер варианта')
    file_ege = models.FileField(upload_to='ege/', verbose_name='Файл варианта')

    def __str__(self):
        return self.title_ege

    class Meta:
        verbose_name = 'Вариант ЕГЭ'
        verbose_name_plural = 'Варианты ЕГЭ'


class BlockAlgebraEge(models.Model):
    title_algebra_ege = models.CharField(max_length=255, verbose_name='Название блока')
    file_algebra_ege = models.FileField(upload_to='algebra/', verbose_name='Файл блока')

    def __str__(self):
        return self.title_algebra_ege

    class Meta:
        verbose_name = 'Программа блока Алгебра ЕГЭ'
        verbose_name_plural = 'Программы блоков Алгебра ЕГЭ'


class BlockGeometriaEge(models.Model):
    title_geometria_ege = models.CharField(max_length=255, verbose_name='Название блока')
    file_geometria_ege = models.FileField(upload_to='geometria/', verbose_name='Файл блока')

    def __str__(self):
        return self.title_geometria_ege

    class Meta:
        verbose_name = 'Программа блока Геометрия ЕГЭ'
        verbose_name_plural = 'Программы блоков Геометрия ЕГЭ'
