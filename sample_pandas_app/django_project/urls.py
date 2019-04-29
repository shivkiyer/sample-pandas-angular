"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', views.NewUser.as_view(), name='new_user'),
    path('api/user/login/', views.user_login, name='login_user'),
    path('api/user/logout/', views.user_logout, name='logout_user'),
    path('api/file-upload/', views.file_upload, name='file-upload'),
    path('api/file-update/', views.file_update, name='file-update'),
    path('api/cancel-upload/', views.cancel_file_upload, name='cancel-file-upload'),
    path('api/fetch-files/', views.fetch_file_list, name='fetch-files'),
    path('api/load-file/', views.load_file, name='load-file'),
]
