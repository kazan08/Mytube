from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password_change/',
        auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), 
        name='password_change'),
    path('password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    path('', views.dashboard, name='dashboard'),
    path('list/', views.ProfileListView.as_view(), name='list'),
    path('<slug:username>/', views.profile, name='profile'),
]
