from taskManager.models import Developer, DeveloperWorkTask, Project, Supervisor, UserProfile, Task
from django.contrib.auth.models import User
import datetime

from django.core.management import BaseCommand


#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    help = "Init taskManager fixtures "

    def handle(self, *args, **options):
        self.stdout.write("start drop")
        drop()
        self.stdout.write("end drop")

        self.stdout.write("start create")
        create()
        self.stdout.write("end create")


def create():
    admin = User.objects.create_superuser(
        username='edil3ra',
        email='edil3ra@gmail.com',
        password='password')
    user1 = User.objects.create_user(
        username='supervisor',
        email='supervisor@gmail.com',
        password='password',
        is_active=True)
    user2 = User.objects.create_user(
        username='vince',
        email='private@gmail.com',
        password='password',
        is_active=True)
    user3 = User.objects.create_user(
        username='fabrice',
        email='private.ouaro@gmail.com',
        password='password',
        is_active=True)

    supervisor1 = Supervisor(
        user_auth=user1,
        phone='0499316385',
        born_date=datetime.date(1982, 10, 10),
        years_seniority=10,
        specialisation='master')

    admin.save()
    supervisor1.save()

    developer1 = Developer(
        user_auth=user2,
        phone='0499316385',
        born_date=datetime.date(1990, 1, 31),
        years_seniority=4,
        sup=supervisor1)
    developer2 = Developer(
        user_auth=user3, phone='0499316499', sup=supervisor1)

    developer1.save()
    developer2.save()

    project1 = Project(
        title='project1',
        description=
        'Nibh sed pulvinar proin gravida hendrerit lectus a molestie lorem ipsum dolor sit amet, consectetur adipiscing elit ut aliquam, purus sit amet. Ipsum dolor sit amet, consectetur adipiscing elit duis.',
        client_name='google')

    project1.save()

    task1 = Task(
        title='task1',
        description=
        'Arcu risus, quis varius quam quisque? Urna neque viverra justo, nec ultrices dui sapien eget mi proin sed libero enim, sed faucibus turpis in eu mi bibendum neque egestas congue.',
        importance=0,
        project=project1, )

    task2 = Task(
        title='task2',
        description=
        'Mi ipsum, faucibus vitae aliquet nec, ullamcorper sit amet. Ornare massa, eget egestas purus viverra accumsan in nisl nisi, scelerisque eu ultrices vitae, auctor eu augue ut lectus arcu, bibendum!',
        importance=1,
        project=project1, )

    task3 = Task(
        title='task3',
        description=
        'Posuere morbi leo urna, molestie at elementum? Enim tortor, at auctor urna nunc id cursus metus aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis orci, a scelerisque purus?',
        importance=2,
        project=project1, )

    task1.save()
    task2.save()
    task3.save()

    developerWorkTask1 = DeveloperWorkTask(
        developer=developer1,
        task=task1,
        time_elapsed=100, )

    developerWorkTask2 = DeveloperWorkTask(
        developer=developer1,
        task=task2,
        time_elapsed=1000, )

    developerWorkTask3 = DeveloperWorkTask(
        developer=developer2,
        task=task1,
        time_elapsed=10, )

    developerWorkTask1.save()
    developerWorkTask2.save()
    developerWorkTask3.save()


def drop():
    User.objects.all().delete()
    UserProfile.objects.all().delete()
    Supervisor.objects.all().delete()
    Developer.objects.all().delete()
    Project.objects.all().delete()
    Task.objects.all().delete()
    DeveloperWorkTask.objects.all().delete()
