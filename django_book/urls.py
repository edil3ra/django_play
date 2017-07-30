"""django_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import CreateView, ListView
from taskManager.models import Project, Task
from django.conf import settings
from django.contrib.auth.decorators import login_required
from taskManager import views as viewsTask


urlpatterns = [
    url(r'^$', viewsTask.index, name='index'),
    url(r'^information/$', viewsTask.information, name='information'),
    url(r'^connection/$', viewsTask.connection, name='connection'),
    url(r'^logout/$', viewsTask.logout, name='logout'),
    url(r'^public_empty/$', viewsTask.public_empty, name='public_empty'),

    url(r'^taskL/$', viewsTask.taskL, name='taskL'),
    url(r'^taskD/(?P<pk>\d+)$', viewsTask.taskD, name='taskD'),
    
    url(r'^createS', viewsTask.createS, name='createS'),
    url(r'^createD', viewsTask.CreateD.as_view(), name='createD'),
    
    url(r'^admin/', admin.site.urls),
    url(r'^create_project/$',
        CreateView.as_view(
            model=Project,
            fields=['title', 'description'],
            template_name='en/public/create_project.html',
            success_url='index'),
        name='create_project'),
    url(r'^create_task/$',
        CreateView.as_view(
            model=Task,
            fields=[
                'title', 'description', 'importance', 'project', 'developers'
            ],
            template_name='en/public/create_task.html',
            success_url='index'),
        name='create_task'),
    url(r'^developer_list$',
        viewsTask.DeveloperListView.as_view(),
        name='developer_list'),
    url(r'^project_list$',
        viewsTask.ProjectListView.as_view(),
        name='project_list'),
    url(r'^task_list$', viewsTask.TaskListView.as_view(), name='task_list'),
    url(r'^task_detail/(?P<pk>\d+)$',
        login_required(viewsTask.TaskDetailView.as_view()),
        name='task_detail'),
    url(r'^developer_detail/(?P<pk>\d+)$',
        viewsTask.DeveloperDetailView.as_view(),
        name='developer_detail'),
    url(r'^update_task_(?P<pk>\d+)$',
        viewsTask.TaskUpdate.as_view(),
        name='task_update'),
    url(r'^update_task_time_(?P<pk>\d+)$',
        viewsTask.TaskUpdateTime.as_view(),
        name='task_update_time')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
