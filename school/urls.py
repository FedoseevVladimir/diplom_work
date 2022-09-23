from django.urls import path
from . import views

urlpatterns = [
    path('online-courses/courses-add/<int:course_id>', views.courses_add, name='courses_add')
]