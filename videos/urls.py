from django.urls import path
from django.conf import settings

from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.VideoListView.as_view(), name='home'),
    path('<int:video_id>/', views.detail, name='detail'),
    path('<int:video_id>/like/', views.like, name='like'),
    path('<int:video_id>/dislike/', views.dislike, name='dislike'),
    path('<int:video_id>/create_comment/', views.create_comment, name='create_comment'),
    path('create_video/', views.create_video, name='create_video'),
]