from django.urls import path,include
from . import views
from .views import send_instruction, view_instructions
urlpatterns = [
    # path('teacher_dashboard/',views.teacher_dashboard,name='teacher_dashboard'),

    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher_add_questions/', views.teacher_add_questions, name='teacher_add_questions'),
    path('teacher_add_subjects/', views.teacher_add_subjects, name='teacher_add_subjects'),
    path('subject_added_page/',views.subject_added_page,name="subject_added_page"),
    path('question_added_page/',views.question_added_page,name="question_added_page"),
    path('view_question/<int:sid>/',views.view_question,name="view_question"),
    path('manage_subjects/',views.manage_subjects,name="manage_subjects"),
    path('manage_questions/',views.manage_questions,name="manage_questions"),
    path('remove_question/<int:sid>',views.remove_question,name="remove_question"),
    path('remove_subject/<int:sid>',views.remove_subject,name="remove_subject"),
    path('send-instruction/', send_instruction, name='send_instruction'),
    path('view-instructions/', view_instructions, name='view_instructions'),

]

