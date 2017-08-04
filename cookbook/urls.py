from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^message$', views.message, name='message'),
    url(r'^notes$', views.NoteList.as_view(), name='notes'),
    url(r'^note(?P<pk>\d+)/$', views.NoteDetail.as_view(), name='note'),
    url(r'^note_create$', views.NoteCreate.as_view(), name='note_create'),
    url(r'^notes$', views.index, name='note_update'),
    url(r'^notes$', views.index, name='note_delete'),
]
