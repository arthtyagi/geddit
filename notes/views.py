from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Notes



def home(request):
    return render(request, 'notes/home.html', {'title':'Home'})

def about(request):
    return render(request, 'notes/about.html', {'title':'About'})

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user).order_by('-last_modified')


class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notes
    success_url = reverse_lazy('notes:list')
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.user:
            return True


class NotesDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Notes
  

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.user:
            return True


class NotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notes
    success_url = reverse_lazy('notes:list')

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.user:
            return True


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    fields = ['title', 'content']
    success_url = reverse_lazy('notes:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
