from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import SSlider, AllCourses, MyCourses
from .forms import OrderForm
from telebot.sendmessage import send_telegram


def first_page(request):
    slider_list = SSlider.objects.all()
    form = OrderForm()
    context = {
        'form': form,
        'slider_list': slider_list
    }
    return render(request, 'school/index.html', context)


def courses(request):
    courses_all = AllCourses.objects.all()
    return render(request, 'school/online-courses.html', {'courses_all': courses_all})


def about_author(request):
    return render(request, 'school/about_author.html')


@login_required(login_url='/users/login/')
def courses_add(request, course_id):
    current_page = request.META.get('HTTP_REFERER')
    course = AllCourses.objects.get(id=course_id)
    my_courses = MyCourses.objects.filter(user=request.user, course=course)
    if not my_courses.exists():
        MyCourses.objects.create(user=request.user, course=course)
        return redirect(current_page)
    else:
        return redirect(current_page)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        service = request.POST['service']
        send_telegram(tg_name=name, tg_phone=phone, tg_service=service)
        return render(request, 'school/thanks.html', {'name': name})
    else:
        return render(request, 'thanks.html')
