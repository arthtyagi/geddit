"""geddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User, Group
admin.autodiscover()

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )

# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

urlpatterns = [
	path('admin/', admin.site.urls),
	path('register/', user_views.register, name='register'),
	path('profile/', user_views.profile, name='profile'),
	path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	path('password-reset/', auth_views.PasswordResetView.as_view(
		template_name='users/password_reset.html'), name='password_reset'),
	path('password-rest/done/', auth_views.PasswordResetDoneView.as_view(
		template_name='users/password_reset_done.html'), name='password_reset_done'),
	path('password-rest-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
		template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
	path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
		template_name='users/password_reset_complete.html'), name='password_reset_complete'),
	path('', include('notes.urls')),
	path('',include('todo.urls')),
	path('api-auth/', include('rest_framework.urls')),
	path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),


# REST FRAMEWORK URLS
	path('api/todo/', include('todo.api.urls', 'todo_api')),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						  document_root=settings.MEDIA_ROOT)
