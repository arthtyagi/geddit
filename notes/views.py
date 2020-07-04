from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from .models import Notes
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


def home(request):
    return render(request, 'notes/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'notes/about.html', {'title': 'About'})


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        object_list = super(NotesListView, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get('q', None)
        if search:
            object_list = object_list.filter(
                Q(title__contains=search, user=self.request.user) |
                Q(content__contains=search, user=self.request.user) |
                Q(category__contains=search, user=self.request.user)
            ).order_by('-last_modified')
            return object_list
        else:
            object_list = Notes.objects.filter(
                user=self.request.user).order_by('-last_modified')
            return object_list


class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notes
    success_url = reverse_lazy('notes:list')
    fields = ['title', 'content', 'category']

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
    fields = ['title', 'content', 'category']
    success_url = reverse_lazy('notes:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NotesLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        obj = get_object_or_404(Notes, pk=pk)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


class NotesLikeAPIToggle(APIView):
    authentication_classes = [SessionAuthentication, ]
    permission_clases = [IsAuthenticated, ]

    def get(self, request, pk=None, format=None):
        obj = get_object_or_404(Notes, pk=pk)
        updated = False
        liked = False
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)

            updated = True
        data = {
            'updated': updated,
            'liked': liked
        }
        return Response(data)
