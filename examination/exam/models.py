from django.db import models
from users.models import StudentProfile
# Create your models here.
class addSubject(models.Model):
    subject = models.CharField(max_length=250)
    total_questions = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.subject
    

class addQuestion(models.Model):
    subject = models.ForeignKey(addSubject, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_ans = (('option1','option1'),('option2','option2'),('option3','option3'),('option4','option4'))
    answer = models.CharField(max_length=200,choices=correct_ans)
    marks = models.IntegerField()

    def __str__(self):
        return self.subject.subject

class Result(models.Model):
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    subject = models.ForeignKey(addSubject, on_delete=models.CASCADE)
    marks = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.user.username
