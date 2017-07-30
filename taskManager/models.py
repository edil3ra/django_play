from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)
    phone = models.CharField(
        max_length=20,
        verbose_name="Phone number",
        null=True,
        default=None,
        blank=True)
    born_date = models.DateField(
        verbose_name="Born date", null=True, default=None, blank=True)
    last_connexion = models.DateTimeField(
        verbose_name="Date of last connection",
        null=True,
        default=None,
        blank=True)
    years_seniority = models.IntegerField(verbose_name="Seniority", default=0)

    
    def __str__(self):
        return self.user_auth.username


class Supervisor(UserProfile):
    specialisation = models.CharField(max_length=50, verbose_name='Specialisation')

    def __str__(self):
        return super().__str__()  + ' Supervisor'
    

    
class Developer(UserProfile):
    sup = models.ForeignKey(Supervisor)
    tasks = models.ManyToManyField("Task", through="DeveloperWorkTask")

    def __str__(self):
        return super().__str__()  + ' Developer'
    
    

class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    client_name = models.CharField(max_length=1000, verbose_name="Client name")

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    importance = models.IntegerField(verbose_name="Importance")
    project = models.ForeignKey(
        Project, verbose_name="Project", null=True, default=None, blank=True)
    developers = models.ManyToManyField(Developer, through="DeveloperWorkTask")

    def __str__(self):
        return self.title

    
class DeveloperWorkTask(models.Model):
    developer = models.ForeignKey(Developer)
    task = models.ForeignKey(Task)
    time_elapsed = models.IntegerField(
        verbose_name="Time elapsed", null=True, default=None, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.developer.user_auth.username, self.task.title)

