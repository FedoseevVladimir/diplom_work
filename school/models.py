from django.db import models


class SSlider(models.Model):
    s_img = models.ImageField(upload_to='slider_img/')
    s_title = models.CharField(max_length=200, verbose_name="Название")
    s_css = models.CharField(max_length=200, null=True, default='-', verbose_name='css класс')

    def __str__(self):
        return self.s_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
