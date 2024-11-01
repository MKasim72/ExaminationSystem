from django.db import models
from users.models import TeacherProfile
from django.contrib.auth.models import User

class Instruction(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

