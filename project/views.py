from django.shortcuts import render
from courses.models import Course, Video
from book.models import BookFile
from home.models import Blog
from django.core.paginator import Paginator
from django.db.models import Q

def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def search_view(request):
    query = request.GET.get('q', '') 
    results = [] 

    if query:
        try:
            courses_results = Course.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) 
            )
        except Exception :
            courses_results = []
        try:
            videos_results = Video.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) | Q(title__icontains=query) 
            )
        except Exception :
            videos_results = []
        try:
            books_results = BookFile.objects.filter(
                Q(name__icontains=query) | Q(title__icontains=query) 
            )
        except Exception :
            books_results = []
        try:
            blog_results = Blog.objects.filter(
                Q(sub_title__icontains=query) | Q(title__icontains=query) 
            )
        except Exception :
            blog_results = []

        results = list(courses_results) + list(videos_results) + list(books_results) + list(blog_results)
    paginator = Paginator(results, 10) 
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    return render(request, 'search_results.html', {
        'query': query,
        'page_obj': page_obj,
    })
