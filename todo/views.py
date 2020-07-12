from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.db.models import Q


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todo'
    paginate_by = 15
    def get_queryset(self, *args, **kwargs):
        object_list = super(TodoListView, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get('q', None)
        if search:
            object_list = object_list.filter(
                Q(title__icontains=search, user=self.request.user) |
                Q(content__icontains=search, user=self.request.user)
            ).order_by('created')
            return object_list
        else:
            object_list = Todo.objects.filter(
                user=self.request.user).order_by('created')
            return object_list


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    template_name = 'todo/todo_update_form.html'
    success_url = reverse_lazy('todo:list')

    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Todo = self.get_object()
        if self.request.user == Todo.user:
            return True


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def test_func(self):
        Todo = self.get_object()
        if self.request.user == Todo.user:
            return True


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'content']
    success_url = reverse_lazy('todo:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
