from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('changes/', views.changes, name='changes'),
    path('admin/file_changes/', views.admin_file_changes, name='admin_file_changes'),
    path('login/', auth_views.LoginView.as_view(template_name='editor/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]