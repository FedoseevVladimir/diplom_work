from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import SSlider, AllCourses, MyCourses


def first_page(request):
    slider_list = SSlider.objects.all()
    return render(request, 'school/index.html', {'slider_list': slider_list})


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
