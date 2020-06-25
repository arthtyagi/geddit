# todo - update the urls.py with private and public mode urls
from django.urls import path
from .import views
from .models import Notes
from .views import NotesCreateView, NotesListView, NotesUpdateView, NotesDeleteView, NotesDetailView

app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', NotesListView.as_view(), name='list'),   
    path('notes/<int:pk>/', NotesDetailView.as_view(), name='detail'),
    path('notes/new/', NotesCreateView.as_view(), name='create'),
    path('notes/<int:pk>/update/', NotesUpdateView.as_view(), name='update'),
    path('notes/<int:pk>/delete/', NotesDeleteView.as_view(), name='delete'),
    path('about/',views.about, name = 'about')
]
