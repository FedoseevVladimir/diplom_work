from django.db import models
from users.models import User


class SSlider(models.Model):
    s_img = models.ImageField(upload_to='slider_img/')
    s_title = models.CharField(max_length=200, verbose_name="Название")
    s_css = models.CharField(max_length=200, null=True, default='-', verbose_name='css класс')

    def __str__(self):
        return self.s_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class AllCourses(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название курса')
    image = models.ImageField(upload_to='school_images', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    short_description = models.CharField(max_length=100, blank=True, verbose_name='Короткое описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
