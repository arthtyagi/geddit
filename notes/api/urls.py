from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from notes.api import views
app_name = 'notes'

urlpatterns = [
    path('', views.NotesList.as_view(), name = 'list' ),
    path('<int:pk>/', views.NotesDetail.as_view(), name = 'detail'),
]

