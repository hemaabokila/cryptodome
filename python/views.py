from django.shortcuts import render
from .models import Codes
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Library
from .serializers import LibrarySerializer ,CodesSerializer

class CodesListView(APIView):
    def get(self, request):
        codes = Codes.objects.all()
        serializer = CodesSerializer(codes, many=True)
        return Response(serializer.data)
    
def codes_page(request):
    return render(request, 'python.html')

class LibraryListView(APIView):
    def get(self, request):
        libraries = Library.objects.all()
        serializer = LibrarySerializer(libraries, many=True)
        return Response(serializer.data)
    
def library_page(request):
    return render(request, 'libraries.html')
