from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
]
