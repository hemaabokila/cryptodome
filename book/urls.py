from django.urls import path
from . views import list_books ,BooklList

urlpatterns = [
    path('', list_books, name='books'),
    path('api/books/', BooklList.as_view(), name='books-list'), 
]
