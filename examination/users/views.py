from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .forms import StudentRegistrationForm, TeacherRegistrationForm, CustomLoginForm


def home(request):
    return render(request, 'home.html')

def student_home_page(request):
    return render(request, 'student_page.html')

def teacher_home_page(request):
    return render(request, 'teacher_page.html')


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration/student_register.html', {'form': form, 'user_type': 'student'})

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'registration/teacher_register.html', {'form': form, 'user_type': 'teacher'})

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            if user.is_student:
                return redirect('student_dashboard')  # Use `redirect` instead of `HttpResponseRedirect`
            elif user.is_teacher:
                return redirect('teacher_dashboard')
        else:
            form = CustomLoginForm()
            return render(request, 'registration/login.html', {'form': form,"error":"Username or password is incorrect"})
            
    else:
        form = CustomLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def custom_logout(request):
    logout(request) 
    return redirect('login')  


