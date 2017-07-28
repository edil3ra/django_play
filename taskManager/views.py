from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView
from .models import Project, Task, Developer, DeveloperWorkTask
from .forms import FormTaskTime


def index(request):
    all_projects = list(Project.objects.all())
    data = {
        'actions': 'Display all projects',
        'projects': all_projects,
    }
    return render(request, 'en/public/index.html', data)


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
    return render(request, 'en/public/connection.html')


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
