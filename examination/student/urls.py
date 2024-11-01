from django.urls import path
from . import views

urlpatterns = [
    path('student_dashboard/', views.student_dashboard, name="student_dashboard"),
    path('start-exam/<sid>/', views.start_exam, name="start_exam"),
    path('view_result/', views.view_result, name="view_result"),
    path('student_exam_select/',views.student_exam_select,name='student_exam_select'),
    path('student_marks/',views.student_marks,name='student_marks'),
    path('check_marks/<int:sid>',views.check_marks,name="check_marks"),
    path('calculate_marks/',views.calculate_marks,name="calculate_marks"),
    path('check_instructions',views.check_instructions,name="check_instructions")
    # path('exam_view/', views.exam_view, name="exam_view"),
]
