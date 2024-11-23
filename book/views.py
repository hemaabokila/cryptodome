from django.shortcuts import render , get_object_or_404
from .models import BookFile
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# api for mobaile app
class BooklList(APIView):
    def get(self, request):
        book = BookFile.objects.all().order_by('-created_at')
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

def list_books(request, book_id=None):
    books = BookFile.objects.all().order_by('-created_at')
    book = None
    if book_id: 
        book = get_object_or_404(BookFile, id=book_id).order_by('-created_at')
    return render(request, 'list_books.html', {'book': book, 'books': books})
