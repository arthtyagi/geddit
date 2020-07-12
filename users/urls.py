from django.urls import path
from . import views
from users.views import SignUpView, AccountDetailView
app_name = 'users'

urlpatterns = [
    path('profile/register/', SignUpView.as_view(), name = 'register'),
	path('profile/edit/', views.profile, name='profile'),
	path('user/<slug:slug>/',AccountDetailView.as_view(), name='profilepage'),
	]
