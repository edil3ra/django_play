from django import forms
from django.forms import ModelForm, Form, ValidationError
from taskManager.models import Task, DeveloperWorkTask, Supervisor, Developer
from django.contrib.auth import authenticate

class FormTaskTime(ModelForm):
    class Meta:
        model = DeveloperWorkTask
        fields = ['time_elapsed', 'developer', 'task']


class FormDeveloper(ModelForm):
    class Meta:
        model  = Developer
        fields = ['user_auth', 'sup', 'tasks']
        
        

class FormSupervisor(Form):
    name = forms.CharField(label="Name", max_length=30)
    login = forms.CharField(label = "Login")
    email = forms.EmailField(label = "Email")
    specialisation = forms.CharField(label = "Specialisation")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data['password']
        password_bis = self.cleaned_data['password_bis']
        if password != password_bis:
            raise ValidationError('Password does not match')
        return self.cleaned_data



class FormConnection(Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise ValidationError('Wrong login or password')
        return self.cleaned_data

