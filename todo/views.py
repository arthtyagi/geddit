from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo


def about(request):
    return render(request, 'todo/about.html', {'title':'About'})

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'Todo'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo

    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Todo = self.get_object()
        if self.request.user == Todo.user:
            return True


class TodoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Todo

    def test_func(self):
        Todo = self.get_object()
        if self.request.user == Todo.user:
            return True


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = '/'

    def test_func(self):
        Todo = self.get_object()
        if self.request.user == Todo.user:
            return True


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
