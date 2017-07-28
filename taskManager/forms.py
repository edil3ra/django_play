from django.forms import ModelForm
from taskManager.models import Task, DeveloperWorkTask


class FormTaskTime(ModelForm):
    class Meta:
        model = DeveloperWorkTask
        fields = ['time_elapsed', 'developer', 'task']
