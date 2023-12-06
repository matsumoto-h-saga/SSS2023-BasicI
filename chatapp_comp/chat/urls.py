from django.contrib import admin
from django.urls import path,include

from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('admin/',admin.site.urls),
]