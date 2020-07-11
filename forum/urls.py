from django.urls import path
from .import views
from .views import QueryCreateView, QueryListView, QueryUpdateView, QueryDeleteView, QueryDetailView, QueryLikeAPIToggle, QueryLikeToggle,AnswerLikeAPIToggle, AnswerLikeToggle, AnswerCreateView, AnswerDeleteView, AnswerUpdateView

app_name = 'forum'

urlpatterns = [
    # forum url
    path('forum/', QueryListView.as_view(), name='list'),
    # query urls
    path('forum/query/<int:pk>/', QueryDetailView.as_view(), name='detail'),
    path('forum/query/new/', QueryCreateView.as_view(), name='query-create'),
    path('forum/query/<int:pk>/update/',
         QueryUpdateView.as_view(), name='query-update'),
    path('forum/query/<int:pk>/delete/',
         QueryDeleteView.as_view(), name='query-delete'),
    path('forum/query/<int:pk>/like/',
         QueryLikeToggle.as_view(), name='query-likes-toggle'),
    path('api/forum/query/<int:pk>/like/',
         QueryLikeAPIToggle.as_view(), name='query-likes-api-toggle'),
    # answer urls
    path('forum/answer/new/', AnswerCreateView.as_view(), name='answer-create'),
    path('forum/answer/<int:pk>/update/',
         AnswerUpdateView.as_view(), name='answer-update'),
    path('forum/answer/<int:pk>/delete/',
         AnswerDeleteView.as_view(), name='answer-delete'),
    path('forum/answer/<int:pk>/like/',
         AnswerLikeToggle.as_view(), name='answer-likes-toggle'),
    path('api/forum/answer/<int:pk>/like/',
         AnswerLikeAPIToggle.as_view(), name='answer-likes-api-toggle'),
]
