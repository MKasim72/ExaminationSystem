from django import forms
from exam.models import addQuestion,addSubject
from django.contrib.auth.models import User
# from django.contrib.auth import User
from .models import Instruction
# from . import models


class AddQuestionForm(forms.ModelForm):
        # subject_id = forms.ModelChoiceField(queryset=addSubject.objects.all(),to_field_name='id')
    class Meta:
        model = addQuestion
        fields = ['subject','question', 'option1', 'option2', 'option3', 'option4', 'answer', 'marks']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'option1': forms.TextInput(attrs={'class': 'form-control'}),
            'option2': forms.TextInput(attrs={'class': 'form-control'}),
            'option3': forms.TextInput(attrs={'class': 'form-control'}),
            'option4': forms.TextInput(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        answer = forms.ChoiceField(choices=addQuestion.correct_ans, label="Answer", widget=forms.Select(attrs={'class': 'form-control'}))

        

    # The 'answer' field should use the choices from the model
    # answer = forms.ChoiceField(choices=addQuestion.correct_ans, label="Answer" )
        

    # Optionally, you can add widgets or custom attributes to the fields:
    # question = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the question here...'}))


class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = addSubject
        fields = ['subject', 'total_questions', 'total_marks']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'total_questions': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_marks': forms.NumberInput(attrs={'class': 'form-control'}),
        }




class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['title', 'message']
