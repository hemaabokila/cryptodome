from django.urls import path
from .views import  library_page, codes_page, LibraryListView ,CodesListView

urlpatterns = [
    path('', codes_page, name='python'),
    path('libraries', library_page, name='library-page'),
    path('api/codes/', CodesListView.as_view(), name='codes-list'), 
    path('api/libraries/', LibraryListView.as_view(), name='library-list'),  
]