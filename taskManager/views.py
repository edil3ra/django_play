from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Project, Task, Developer, DeveloperWorkTask, Supervisor
from .forms import FormTaskTime, FormSupervisor, FormDeveloper, FormConnection


def index(request):
    all_projects = list(Project.objects.all())
    data = {
        'actions': 'Display all projects',
        'projects': all_projects,
    }
    
    return render(request, 'en/public/index.html', data)


@login_required
def information(request):
    my_variable = 'Hello World'
    years_old = 27
    array_city_capitale = ['Paris', 'London', 'Washigton']
    data = {
        'my_var': my_variable,
        'years': years_old,
        'cities': array_city_capitale,
        'xss': '<script>console.log("hello world")</script>'
    }
    return render(request, 'en/public/information.html', data)


def connection(request):
    if request.method == 'POST':
        form = FormConnection(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
        return render(request, 'en/public/connection.html', {'form': form})
    else:
        form = FormConnection()
        return render(request, 'en/public/connection.html', {'form' : form})


def logout(request):
    auth.logout(request)
    return render(request, 'en/public/logout.html')

    
def public_empty(request):
    return render(request, 'en/public/empty.html')


def taskL(request):
    tasks = Task.objects.all().order_by('importance').reverse()
    current_task_id = request.session.get('last_task') or 0
    current_task = Task.objects.filter(id=current_task_id).get()
    data = {
        'tasks': tasks,
        'task': current_task,
    }
    return render(request, 'en/public/taskL.html', data)



def taskD(request, pk):
    task = Task.objects.filter(id=pk)
    try:
        task = task.get()
    except (Task.DoesNotExist, Task.MultipleObjectReturned):
        return redirect('information')
    else:
        request.session['last_task'] = task.id
    return render(request, 'en/public/taskD.html', {'task': task})



def createS(request):
    if request.method == 'POST':
        form = FormSupervisor(request.POST)
        if(form.is_valid()):
            name = form.cleaned_data['name']
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            specialisation = form.cleaned_data['specialisation']
            password = form.cleaned_data['password']
            password_bis = form.cleaned_data['password_bis']
            user =  User.objects.create_user(username=login, email=email, password=password)
            user.is_active = True
            user.last_name = name
            user.save()
            
            supervisor = Supervisor(user_auth=user, specialisation=specialisation)
            supervisor.save()
            
            return redirect('public_empty')
        else:
            return render(request, 'en/public/create_supervisor.html', {'form': form})
    else:
        form = FormSupervisor()
        return render(request, 'en/public/create_supervisor.html', {'form': form})


class CreateD(CreateView):
    form_class = FormDeveloper
    template_name='en/public/create_task.html'


class ProjectListView(ListView):
    paginate_by = 5
    template_name = 'en/public/project_list.html'
    queryset = Project.objects.all().order_by('title')


class TaskListView(ListView):
    paginate_by = 2
    template_name = 'en/public/task_list.html'
    queryset = Task.objects.all()


class DeveloperListView(ListView):
    template_name = 'en/public/developer_list.html'
    model = Developer


class TaskDetailView(DetailView):
    template_name = 'en/public/task_detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        developers = Developer.objects.filter(task=self.object)
        context['developers'] = developers
        return context


class DeveloperDetailView(DetailView):
    template_name = 'en/public/developer_detail.html'
    model = Developer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks_dev = Task.objects.filter(developer=self.object)
        context['tasks_dev'] = tasks_dev
        return context


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'en/public/update_task_developer.html'
    success_url = 'index'


class TaskUpdateTime(UpdateView):
    model = DeveloperWorkTask
    template_name = 'en/public/update_task_developer_time.html'
    form_class = FormTaskTime
    success_url = reverse_lazy('task_update_time', kwargs={'pk': model.pk})

    # def get_success_url(self):
    #     return self.success_url
