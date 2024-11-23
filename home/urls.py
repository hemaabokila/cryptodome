from django.urls import path
from .views import  blog_list,home_view, BlogList 

urlpatterns = [
    path('', home_view, name='home'), 
    path('blog/<slug:blog_slug>/', blog_list, name='blog_list'), 
    path('api/blog/', BlogList.as_view(), name='api-blog-list'), 
]