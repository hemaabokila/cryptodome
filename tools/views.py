from django.shortcuts import render
from .models import Tool
from .serializers import ToolSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# api for mobaile app
class ToolList(APIView):
    def get(self, request):
        tool = Tool.objects.all()
        serializer = ToolSerializer(tool, many=True)
        return Response(serializer.data)


def tool(request):
    tools = Tool.objects.all()
    return render(request, 'tools.html', {'tools': tools})