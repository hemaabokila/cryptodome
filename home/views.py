from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from courses.models import Video, Course
from tools.models import Tool
from book.models import BookFile
from .models import Blog, AppVisit
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum, Q
from datetime import date
import requests
from django.shortcuts import render

def youtube_stats(request):
    API_KEY = "API_KEYAIzaSyBkyCbWcchtVMTqlJC2JWXJjITr8rMk0Ak"
    CHANNEL_ID = "CHANNEL_ID"  

    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    stats = data["items"][0]["statistics"]
    subscriber_count = stats.get("subscriberCount", "N/A")
    view_count = stats.get("viewCount", "N/A")
    context = {
        "subscriber_count": subscriber_count,
        "view_count": view_count,
    }

    return render(request, "home.html", context)

class BlogPagination(PageNumberPagination):
    page_size = 10

# API for mobile app
class BlogList(APIView):
    def get(self, request):
        try:
            blogs = Blog.objects.all()
            paginator = BlogPagination()
            result_page = paginator.paginate_queryset(blogs, request)
            serializer = BlogSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({'error': 'Something went wrong'}, status=500)

# View for blog details
def blog_list(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    return render(request, 'blog.html', {'blog': blog})

# Home page view
def home_view(request):
    cached_data = cache.get('home_data')

    if not cached_data:
        visits = AppVisit.objects.filter(app_name="home").aggregate(
            today_visits=Sum('visit_count', filter=Q(date=date.today())),
            total_visits=Sum('visit_count')
        )
        
        latest_videos = Video.objects.order_by('-created_at')[:6]
        latest_courses = Course.objects.order_by('-created_at')[:6]
        latest_tools = Tool.objects.order_by('-created_at')[:8]
        latest_book = BookFile.objects.order_by('-created_at')[:8]
        latest_blog = Blog.objects.order_by('-created_at')[:8]

        API_KEY = "AIzaSyBkyCbWcchtVMTqlJC2JWXJjITr8rMk0Ak"  
        CHANNEL_ID = "UCDVKXBObm1NQFVWsR38S1mQ" 

        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
            stats = data["items"][0]["statistics"]
            subscriber_count = stats.get("subscriberCount", "N/A")
            view_count = stats.get("viewCount", "N/A")
        except Exception as e:
            subscriber_count = "N/A"
            view_count = "N/A"

        cached_data = {
            'today_visits': visits['today_visits'] or 0,
            'total_visits': visits['total_visits'] or 0,
            'latest_videos': latest_videos,
            'latest_courses': latest_courses,
            'latest_tools': latest_tools,
            'latest_book': latest_book,
            'latest_blog': latest_blog,
            'subscriber_count': subscriber_count,
            'view_count': view_count,
        }

        cache.set('home_data', cached_data, 300) 

    return render(request, 'home.html', cached_data)
