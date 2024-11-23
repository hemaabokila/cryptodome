from rest_framework import serializers
from .models import BookFile

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        fields = '__all__'

