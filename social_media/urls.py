from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('signup/', views.signup, name='signup'),  # Custom signup view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
