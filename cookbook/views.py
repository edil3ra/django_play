from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib import messages

from .forms import MessageForm, InspirationQuoteForm
from .models import Note, InspirationQuote


def index(request):
    return render(request, 'index.html')


def message(request):
    if request.method == 'POST':
        form = MessageForm(request ,request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "message corretly send")
            return redirect('message')
    else:
        form = MessageForm(request)
    return render(request, 'message.html', {'form': form })


def add_quote(request):
    if request.method == 'POST':
        form = InspirationQuote(
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            quote = form.save()
            return redirect('add_quote_done')
    else:
        form = InspirationQuoteForm()
    return render(request, 'change_quote.html', {'form': form})
        
    

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

