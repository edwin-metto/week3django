from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
