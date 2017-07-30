from django.contrib import admin
from taskManager.models import Developer, Project, Supervisor, Task, UserProfile, DeveloperWorkTask

admin.site.register(UserProfile)
admin.site.register(Developer)
admin.site.register(Project)
admin.site.register(Supervisor)
admin.site.register(Task)
admin.site.register(DeveloperWorkTask)
