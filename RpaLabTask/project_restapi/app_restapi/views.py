from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import AppPostSerializer
from rest_framework import permissions
from .models import AppPost 

# Create your views here.
class AppPostViews(APIView):
    def get(self, request):
        data_set = AppPost.objects.all()
        serializer = AppPostSerializer(data_set, many=True)

        context = {
            "status_code": 200,
            "message": "Post List",
            "data": serializer.data,
            "error": [],
            "pagination": "",
            "files": [],
            
        }
        return Response(context, status=status.HTTP_200_OK)

    
    def post(self, request):
        if request.method != "POST":
            return Response({
                "status_code": 405, 
                "message": "Method Not Allowed"}, \
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            permission_classes = [permissions.IsAuthenticated]
            serializer = AppPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppPostViewsById(APIView):
    def get_object(self, id):
        try:
            return AppPost.objects.get(id=id)
        except AppPost.DoesNotExist as e:
            return Response({"error": "Not found."},status=404)

    def put(self, request, id=None):    
        data = request.data            # Data passed to overwrite
        instance = self.get_object(id)   
        serializer = AppPostSerializer(instance, data=data)   
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id=None):
        instance = self.get_object(id)
        serializer = AppPostSerializer(instance)
        instance.delete()
        return Response(serializer.data)