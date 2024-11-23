from django.urls import path
from .views import tool ,ToolList

urlpatterns = [
    path('', tool, name='tool'), 
    path('api/tools/', ToolList.as_view(), name='tools-list'), 
]