from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from exam.models import addQuestion, addSubject,Result
from users.models import StudentProfile,TeacherProfile
from teacher.models import Instruction
# Create your views here.

@login_required()
def student_dashboard(request):
    # subjects = addSubject.objects.all()
    subjects = {
         'total_questions':addQuestion.objects.all().count(),
         'total_subjects':addSubject.objects.all().count()
    }
    return render(request, 'student/student_dashboard.html', {'subjects': subjects})
    # return render(request, 'student/student_dashboard.html')

@login_required()
def student_exam_select(request):
     subjects = addSubject.objects.all()
     return render(request, 'student/student_exam_select.html', {'subjects': subjects})
     
@login_required()
def student_marks(request):
     subjects = addSubject.objects.all()
     return render(request, 'student/student_marks.html',{'subjects':subjects})


@login_required()
def calculate_marks(request):
        # subjec0t = addSubject.object.get
        subjects = addSubject.objects.all()
        if request.COOKIES.get('subject_id') is not None:
            subject_id=request.COOKIES.get('subject_id')
            subject = addSubject.objects.get(id=subject_id)
            total_marks = 0
            questions = addQuestion.objects.all().filter(subject=subject) 
            for i in range(len(questions)):
                answer = questions[i].answer
                user_answer = request.COOKIES.get(str(i+1))
                if user_answer == answer:
                     total_marks = total_marks + questions[i].marks
            student = StudentProfile.objects.get(user_id=request.user.id)
            result = Result()
            result.marks = total_marks
            result.student = student
            result.subject = subject
            result.save()
          #   return HttpResponseRedirect('view_result')
        return render(request, 'student/view_result.html',{'total_marks':total_marks,'subjects':subjects})
    
@login_required()   
def view_result(request):
     subject = addSubject.objects.all()
     return render(request,'student/view_result.html',{"subject":subject})

@login_required()
def check_marks(request,sid):
     subjects = addSubject.objects.all()
     subject = addSubject.objects.get(id=sid)
     student = StudentProfile.objects.get(user_id=request.user.id)
     results = Result.objects.all().filter(student=student).filter(subject=subject)
     return render(request,'student/check_marks.html',{'results':results,'total_marks':subjects})
     

@login_required()
def start_exam(request, sid):
    subject = addSubject.objects.get(id=sid)
    questions = addQuestion.objects.all().filter(subject=subject)
    if request.method == 'post':
         pass
    context = {
        'questions': questions,
        'subject': subject,
        'sid': sid  # Pass the subject ID to the template
    }
    res =  render(request, 'student/start_exam.html', context)
    res.set_cookie('subject_id',subject.id)
    return res

@login_required()
def check_instructions(request):
     instructions = Instruction.objects.all()
     return render(request, 'student/check_instructions.html',{'instructions':instructions})