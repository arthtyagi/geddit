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
	path('oauth/', include('social_django.urls', namespace= 'social')),
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
	path('api/notes/', include('notes.api.urls', 'notes_api')),		
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						  document_root=settings.MEDIA_ROOT)
	urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

