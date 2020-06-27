from django.urls import path
from .import views
from .views import TodoCreateView, TodoListView, TodoUpdateView, TodoDeleteView, TodoDetailView

app_name = 'todo'

urlpatterns = [
	path('todo/', TodoListView.as_view(), name='list'),
	path('api/', views.apiOverview, name = 'api'),
	path('todo/<int:pk>/', TodoDetailView.as_view(), name='detail'),
	path('todo/new/', TodoCreateView.as_view(), name='create'),
	path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='update'),
	path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='delete')
	]
