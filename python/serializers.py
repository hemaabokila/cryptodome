from rest_framework import serializers
from .models import Library ,Codes

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = '__all__'