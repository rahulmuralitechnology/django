from rest_framework import serializers
from app.models import test

class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'