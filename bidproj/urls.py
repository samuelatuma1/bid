from django.urls import path
from . import views
app_name = 'bidproj'
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('', views.index, name='index'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('register', views.register, name='register'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
]