from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib import messages

from .forms import MessageForm
from .models import Note


def index(request):
    return render(request, 'index.html')


def message(request):
    if request.method == 'POST':
        form = MessageForm(requst ,request.POST)
        if form.is_valid():
            messages.info('the form successfully passed')
            return redirect('message')
    else:
        form = MessageForm(request)
    return render(request, 'message.html', {'form': form })


class NoteList(ListView):
    model = Note
    template_name = 'notes.html'

class NoteDetail(DetailView):
    model = Note

    
class NoteCreate(CreateView):
    model = Note

    
class NoteUpdate(UpdateView):
    model = Note


class NoteDelete(DeleteView):
    model = Note

