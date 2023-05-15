from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import test
from .serializers import testSerializer

# Create your views here.

@api_view(['GET'])
def get(request):
    data = test.objects.all()
    serializer = testSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def post(request):
    serializer = testSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])

def put(request):
    serializer = testSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)