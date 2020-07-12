# todo - update the urls.py with private and public mode urls
from django.urls import path
from .import views
from .views import NotesCreateView, NotesListView, NotesUpdateView, NotesDeleteView, NotesDetailView, NotesLikeAPIToggle, NotesLikeToggle
app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', NotesListView.as_view(), name='list'),
    path('notes/new/', NotesCreateView.as_view(), name='create'),
    path('notes/<slug:slug>/delete/', NotesDeleteView.as_view(), name='delete'),
    path('notes/<slug:slug>/', NotesDetailView.as_view(), name='detail'),
    path('notes/<slug:slug>/update/', NotesUpdateView.as_view(), name='update'),
    path('notes/<slug:slug>/like/', NotesLikeToggle.as_view(), name='likes-toggle'),
    path('api/notes/<slug:slug>/like/',
         NotesLikeAPIToggle.as_view(), name='likes-api-toggle'),
    path('about/', views.about, name='about')
]
