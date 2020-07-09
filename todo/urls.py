from django.urls import path
from .views import TodoCreateView, TodoListView, TodoUpdateView, TodoDeleteView
app_name = 'todo'

urlpatterns = [
	path('todo/', TodoListView.as_view(), name='list'),
	path('todo/<int:pk>/', TodoUpdateView.as_view(), name='update'),
	path('todo/new/', TodoCreateView.as_view(), name='create'),
	path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='delete')
	]
