from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from exam.models import addQuestion,addSubject
from .forms import AddQuestionForm,AddSubjectForm
from users.models import StudentProfile,TeacherProfile 
# from .models import Teacher
# Create your views here.

@login_required
def teacher_dashboard(request):
    # subjects = addSubject.objects.all()
    subjects = {
         'total_questions':addQuestion.objects.all().count(),
         'total_subjects':addSubject.objects.all().count(),
         'total_students':StudentProfile.objects.all().count(),
    }
    return render(request, 'teacher/teacher_dashboard.html', {'subjects': subjects})

def manage_subjects(request):
    return render(request,'teacher/manage_subjects.html')

def teacher_add_subjects(request):
    if request.method == 'POST':
        subject_form = AddSubjectForm(request.POST)
        if subject_form.is_valid():
            subject_form.save()
            return redirect('subject_added_page')
            # return render(request,'teacher/subject_added_page.html')
        else:
            print("form invalid")
    else:
        subject_form = AddSubjectForm()
    return render(request,'teacher/teacher_add_subjects.html',{'subject_form':subject_form})

def subject_added_page(request):
    subjects = addSubject.objects.all()
    return render(request,'teacher/subject_added_page.html',{'subjects':subjects})


def manage_questions(request):
    return render(request,'teacher/manage_questions.html')


def question_added_page(request):
    subjects = addSubject.objects.all()
    questions = addQuestion.objects.all()
    return render(request,'teacher/question_added_page.html',{'subjects':subjects,'questions':questions})


def teacher_add_questions(request):
    if request.method == 'POST':
        question_form = AddQuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            return redirect('question_added_page')
        else:
            print("Erors in your program ",question_form.errors)
    else:
        question_form = AddQuestionForm()  # Show the form for GET requests
    
    return render(request, 'teacher/teacher_add_questions.html', {'form': question_form})

def view_question(request,sid):
    questions = addQuestion.objects.all().filter(id=sid)
    return render(request,'teacher/view_question.html',{'questions':questions})


def subject_submit(request):
    if request.method == 'POST':
        subject_form = AddSubjectForm(request.POST)
        if subject_form.is_valid():
            subject_form.save()
            return redirect('teacher_dashboard')
        else:
            return render(request,'teacher/subject_submit.html',{'subject_form':subject_form})
    else:
            subject_form = AddSubjectForm()
            return render(request,'teacher/teacher_dashboard.html',{'subject_form':subject_form})

def remove_subject(request,sid):
    subject = addSubject.objects.get(id=sid)
    subject.delete()
    return redirect('subject_added_page')

def remove_question(request,sid):
    question = addQuestion.objects.get(id=sid)
    question.delete()
    return render(request,"teacher/question_added_page.html")



from .forms import InstructionForm
from .models import Instruction


@login_required
def send_instruction(request):
    if request.method == 'POST':
        form = InstructionForm(request.POST)
        if form.is_valid():
            instruction = form.save(commit=False)
            instruction.teacher = TeacherProfile.objects.get(user=request.user)
            instruction.save()
            return redirect('teacher_dashboard')  # Change this to your success URL
    else:
        form = InstructionForm()

    return render(request, 'teacher/send_instruction.html', {'form': form})

def view_instructions(request):
    instructions = Instruction.objects.all()
    return render(request, 'teacher/view_instructions.html', {'instructions': instructions})

@login_required
def view_instructions(request):
    # Assuming you want to filter instructions by the teacher associated with the student
    # Adjust this according to your actual logic
    instructions = Instruction.objects.filter(teacher=request.user)
    return render(request, 'student/view_instructions.html', {'instructions': instructions})
