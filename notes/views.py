from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Notes
from django.db.models import Q


def home(request):
	return render(request, 'notes/home.html', {'title': 'Home'})


def about(request):
	return render(request, 'notes/about.html', {'title': 'About'})


class NotesListView(LoginRequiredMixin, ListView):
	model = Notes
	context_object_name = 'notes'

	def get_queryset(self, *args, **kwargs):
		object_list = super(NotesListView, self).get_queryset(*args, **kwargs)
		search = self.request.GET.get('q', None)
		if search:
			object_list = object_list.filter( 
				Q(title__contains=search, user = self.request.user)|
				Q(content__contains=search, user = self.request.user)|
				Q(category__contains=search, user = self.request.user)	
				).order_by('-last_modified')
			return object_list
		else:
			object_list = Notes.objects.filter(user=self.request.user).order_by('-last_modified')
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

