from django.contrib.sitemaps import Sitemap
from .models import Blog
from courses.models import Course
from tools.models import Tool
from book.models import BookFile
from book.models import BookFile
from django.urls import reverse



class HomePageSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return reverse('home')  

class CoursePageSitemap(Sitemap):
    def items(self):
        return Course.objects.all()

    def location(self, obj):
        return reverse('course_list')  
    
class BookPageSitemap(Sitemap):
    def items(self):
        return BookFile.objects.all()

    def location(self, obj):
        return reverse('books')  
    
class ToolPageSitemap(Sitemap):
    def items(self):
        return Tool.objects.all()

    def location(self, obj):
        return reverse('tool')  

