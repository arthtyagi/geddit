# todo - update the urls.py with private and public mode urls
from django.urls import path
from .import views
from .views import queryCreateView, queryListView, queryUpdateView, queryDeleteView, queryDetailView, queryLikeAPIToggle, queryLikeToggle
app_name = 'query'

urlpatterns = [
    path('query/', queryListView.as_view(), name='list'),
    path('query/<int:pk>/', queryDetailView.as_view(), name='detail'),
    path('query/new/', queryCreateView.as_view(), name='create'),
    path('query/<int:pk>/update/', queryUpdateView.as_view(), name='update'),
    path('query/<int:pk>/like/', queryLikeToggle.as_view(), name='likes-toggle'),
    path('api/query/<int:pk>/like/',
         queryLikeAPIToggle.as_view(), name='likes-api-toggle'),
    path('query/<int:pk>/delete/', queryDeleteView.as_view(), name='delete'),
]
