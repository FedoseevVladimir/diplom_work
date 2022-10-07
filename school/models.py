from django.db import models
from users.models import User


class SSlider(models.Model):
    s_img = models.ImageField(upload_to='slider_img/')
    s_css = models.CharField(max_length=200, null=True, default='-', verbose_name='css класс')

    def __str__(self):
        return self.s_css

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class AllCourses(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название курса')
    image = models.ImageField(upload_to='school_images', blank=True, verbose_name='Изображение')
    image_desc = models.TextField(blank=True, verbose_name='Описание картинки')
    description = models.TextField(blank=True, verbose_name='Описание')
    tg_url = models.CharField(max_length=300, default='#', verbose_name='Курс в телеграмм')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class MyCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    create_buy = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Покупка для {self.user.username} | Курс {self.course.name}'

    class Meta:
        verbose_name = 'Купленный курс'
        verbose_name_plural = 'Купленные курсы'
