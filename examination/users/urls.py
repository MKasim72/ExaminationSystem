from django.urls import path,include
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('student_page/',views.student_home_page,name="student_home_page"),
    path('teacher_page/',views.teacher_home_page,name="teacher_home_page"),
    path('register/student/', views.register_student, name='register_student'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    path('login/', views.custom_login, name='login'),
    # path('logout/', views.custom_logout, name='logout'),
    path('logout/', views.custom_logout, name='custom_logout'),  
    # path('student/dashboard/',include('student.urls'), name='student_dashboard'),
    # path('student/', include('student.urls'), name='student_dashboard'),
    # path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
]
