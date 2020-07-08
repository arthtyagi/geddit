from django.contrib import admin
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
	path('admin/', admin.site.urls),
	path('register/', user_views.SignUpView.as_view(), name='register'),
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
	path('ckeditor/', include('ckeditor_uploader.urls')),


# REST FRAMEWORK URLS
	path('api/todo/', include('todo.api.urls', 'todo_api')),
	path('api/notes/', include('notes.api.urls', 'notes_api')),		
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						  document_root=settings.MEDIA_ROOT)
	urlpatterns+= static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

