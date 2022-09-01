from django.shortcuts import render
from .models import SSlider


def first_page(request):
    slider_list = SSlider.objects.all()
    return render(request, 'school/index.html', {'slider_list': slider_list})