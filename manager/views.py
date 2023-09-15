from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Project, Student, Result
from django.contrib import messages
import os
from django.conf import settings

# Create your views here.
def Home(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_password = request.POST.get('student_password')


        try:
            user = authenticate(request, groups=2, username=student_id, password=student_password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully !')
                return redirect('student')

            else:
                print('User is not a Student...')

        except Exception as e:
            print('User not found...')

    return render(request, 'manager/home.html')

@login_required
def StudentDashboard(request):
    student = Student.objects.get(name=request.user)
    projects = Project.objects.filter(level=student.level)
    results = Result.objects.filter(student_id=student.id_number)
    if projects:
        header = 'Pending Projects'
    else:
        header = 'No Projects Pending'
    print(header)
    context = {
        'header' : header,
        'student' : student,
        'user' : request.user,
        'projects': projects,
        'results' : results,
    }
    return render(request, 'manager/student.html', context)

@login_required
def Staff(request):
    #print(Result.objects.all())
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        author = request.POST.get('author')
        level = request.POST.get('level')

        data = Project(title=title, body=body, author=author, level=level)
        data.save()

        student_id = request.POST.get('student_id')
        img = request.FILES('img')

        data1 = Result.objects.create(student_id=student_id, img=img)
        data1.save()

    context = {
        'user': request.user,
    }
    return render(request, 'manager/staff.html')

def StaffLogin(request):

    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        staff_password = request.POST.get('staff_password')


        try:
            user = User.objects.get(username=staff_id, groups=2)

            user = authenticate(request, groups=2, username=staff_id, password=staff_password)
            group = Group.objects.all()

            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully !')
                return redirect('staff')

            else:
                print('User is not a Staff...')

            print(f'{user} is good to go...')

        except Exception as e:
            print('User not found...')

    return render(request, 'manager/staff_login.html')

def custom_404(request, exception):
    return render(request, 'manager/404.html')

def StudentDetail(request):
    return render(request, 'manager/student_detail.html')
def Projects(request):
    student = Student.objects.get(name=request.user)
    print(student.level)
    context = {
        'projects': Project.objects.filter(level=student.level)
    }
    return render(request, 'manager/project.html', context)
