from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's authentication views
from .views import home, about_me, profile, profile_1, add_work_experience, update_work_experience, update_profile

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name = 'home'),
    path('home/', home, name = 'home'),
    path('about_me', about_me, name= 'about_me'),
    path('profile/', profile, name = 'profile'),
    path('profile_1/', profile_1, name = 'profile_1'),
    path('update_profile/', update_profile, name='update_profile'),
    path('add_work_experience/', add_work_experience, name='add_work_experience'),
    path('update_work_experience/<int:pk>/', update_work_experience, name='update_work_experience'),
]