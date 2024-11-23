from django.shortcuts import render ,get_object_or_404
from .models import Course, Video
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer ,VideoSerializer

# api for mobaile app
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all().order_by('-created_at')
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

class VideoListView(APIView):
    def get(self, request):
        videos = Video.objects.all().order_by('-created_at')
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

class VideoDetailView(APIView):
    def get(self, request, video_id):
        try:
            video = Video.objects.get(id=video_id)
            serializer = VideoSerializer(video)
            return Response(serializer.data)
        except Video.DoesNotExist:
            return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)
    
def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'course_list.html', {'courses': courses})

def course_videos(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    videos = course.videos.all().order_by('-created_at') 
    return render(request, 'course_videos.html', {'course': course, 'videos': videos})

def video_detail(request, course_slug, video_slug):
    course = get_object_or_404(Course, slug=course_slug)
    video = get_object_or_404(Video, slug=video_slug, course=course)
    return render(request, 'video_detail.html', {'course': course, 'video': video})
