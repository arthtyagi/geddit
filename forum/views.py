from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from .models import Query, Answer
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class QueryListView(ListView):
    model = Query
    template_name = "forum/query_list.html"
    paginate_by = 15
    context_object_name = 'query'
    ordering = ['-last_modified']


    def get_queryset(self, *args, **kwargs):
        object_list = super(QueryListView, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get('q', None)
        if search:
            object_list = object_list.filter(
                Q(title__contains=search) |
                Q(content__contains=search) |
                Q(category__contains=search)
            ).order_by('-last_modified')
            return object_list
        else:
            return object_list


class QueryDetailView(DetailView):
    model = Query
    context_object_name = 'query'
    template_name = "forum/query_detail.html"


class QueryCreateView(LoginRequiredMixin, CreateView):
    model = Query
    template_name = "forum/query_form.html"
    fields = ['title', 'content', 'category']
    success_url = reverse_lazy('forum:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QueryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Query
    success_url = reverse_lazy('forum:list')
    fields = ['title', 'content', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        query = self.get_object()
        if self.request.user == query.user:
            return True


class QueryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Query
    success_url = reverse_lazy('forum:list')

    def test_func(self):
        query = self.get_object()
        if self.request.user == query.user:
            return True


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    template_name = "forum/answer_form.html"
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnswerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Answer
    success_url = reverse_lazy('forum:list')
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.user:
            return True


class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    success_url = reverse_lazy('forum:list')

    def test_func(self):
        query = self.get_object()
        if self.request.user == query.user:
            return True


class QueryLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        obj = get_object_or_404(Query, pk=pk)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


class QueryLikeAPIToggle(APIView):
    authentication_classes = [SessionAuthentication, ]
    permission_clases = [IsAuthenticated, ]

    def get(self, request, pk=None, format=None):
        obj = get_object_or_404(Query, pk=pk)
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


class AnswerLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        obj = get_object_or_404(Answer, pk=pk)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


class AnswerLikeAPIToggle(APIView):
    authentication_classes = [SessionAuthentication, ]
    permission_clases = [IsAuthenticated, ]

    def get(self, request, pk=None, format=None):
        obj = get_object_or_404(Answer, pk=pk)
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
