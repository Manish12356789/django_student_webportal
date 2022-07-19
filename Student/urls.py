from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-students', views.all_students, name='all_students'),
    path('add-student', views.add_student, name='add_student'),
    path('student-save', views.student_save, name='student_save'),
    path('student-edit/<str:slug>', views.edit_student, name='edit_student'),
    path('student-edit/update/<str:slug>', views.update_student, name='update_student'),
    path('student-delete/<str:slug>', views.delete_student, name='delete_student'),
]