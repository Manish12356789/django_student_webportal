from pyexpat.errors import messages
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Student.decorators import allowed_users


from django.http import HttpResponse

from .models import Student

@login_required(login_url='login')
@allowed_users(allowed_roles=['superadmin', 'admin', 'user'])
def index(request):
    students = Student.objects.all()
    student_count = Student.objects.all().count()
    context = {'students' : students, 'student_count': student_count}
    return render(request, 'home.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['superadmin', 'admin', 'user'])
def all_students(request):
    students = Student.objects.all()
    context={'students' : students}    
    return render(request, 'all_students.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['superadmin', 'admin'])
def add_student(request):
    return render(request, 'add_student.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['superadmin', 'admin'])
def student_save(request):
    if request.method=='POST':
        s_fname=request.POST['fname']
        s_lname=request.POST['lname']
        s_email=request.POST['email']
        s_gender=request.POST['gender']
        slug = slugify(s_fname + '-' + s_lname)
        student=Student(
            s_fname=s_fname, 
            s_lname=s_lname, 
            s_email=s_email, 
            s_gender=s_gender, 
            slug=slug
        )
        student.save()
        # messages.success(request,'Data has been submitted')
    return HttpResponseRedirect(reverse('all_students'))

@login_required(login_url='login')
@allowed_users(allowed_roles=['superadmin', 'admin'])
def edit_student(request, slug):
    student = Student.objects.get(slug=slug)
    context = {'student': student}
    return render(request, 'edit_student.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['superadmin', 'admin'])
def update_student(request, slug):
    s_fname=request.POST['fname']
    s_lname=request.POST['lname']
    s_email=request.POST['email']
    s_gender=request.POST['gender']

    student = Student.objects.get(slug=slug)
    student.s_fname=s_fname, 
    student.s_lname=s_lname, 
    student.s_email=s_email, 
    student.s_gender=s_gender, 
    student.save()
    return HttpResponseRedirect(reverse('all_students'))

@login_required(login_url='login')
@allowed_users(allowed_roles=['superadmin', 'admin'])
def delete_student(request, slug):
    student = Student.objects.get(slug=slug)
    student.delete()
    return HttpResponseRedirect(reverse('all_students'))