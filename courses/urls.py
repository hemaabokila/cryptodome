from django.urls import path
from .views import CourseListView, VideoListView,VideoDetailView, course_list, course_videos, video_detail

urlpatterns = [
    path('', course_list, name='course_list'),
    path('course/<slug:course_slug>/videos/', course_videos, name='course_videos'),
    path('course/<slug:course_slug>/video/<slug:video_slug>/', video_detail, name='video_detail'),
    path('api/course/', CourseListView.as_view(), name='course-list'),  
    path('api/videos/', VideoListView.as_view(), name='video-list'), 
    path('api/video/<int:video_id>/', VideoDetailView.as_view(), name='VideoDetailView'), 
]
