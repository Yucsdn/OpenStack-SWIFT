from django.urls import path
from . import views

app_name = 'ycl0310'
urlpatterns = [
    path('login/', views.login),
    path('get_token/', views.get_token),
    path('add_file/', views.add_file),
    path('delete_down/', views.delete_down),
    path('home/', views.home),
    path('sousuo/', views.sousuo),
    path('open_file_path/', views.open_file_path),
    path('home/see_file/', views.see_file, name='see_file'),
    path('home/image/', views.image, name='image'),
    path('home/txt/', views.txt, name='txt'),
    path('home/video/', views.video, name='video'),
    path('home/download/', views.download, name='download'),
]