from django import forms
from .models import User, StudentProfile, TeacherProfile
from django.contrib.auth.forms import AuthenticationForm

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_student = True
        if commit:
            user.save()
            StudentProfile.objects.create(user=user)
        return user

class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_teacher = True
        if commit:
            user.save()
            TeacherProfile.objects.create(user=user)
        return user


class CustomLoginForm(AuthenticationForm):
    # def __init__(self, *args, **kwargs):
    #     super(CustomLoginForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget = forms.TextInput(attrs={
    #         'class': 'form-control custom-input text-center border-3', 
    #         'placeholder': 'Username'
    #     })
    #     self.fields['password'].widget = forms.PasswordInput(attrs={
    #         'class': 'form-control custom-input text-center border-3', 
    #         'placeholder': 'Password'
    #     })
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control custom-input text-center border-3','placeholder':'Username'}))
    password = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'class': 'form-control custom-input text-center border-3', 
    'placeholder': 'Password'}))

