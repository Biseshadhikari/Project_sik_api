from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializer import *
from core.models import *

from rest_framework.response import Response


class CreateCategory(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RetrieveCategory(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request): 
        category = Category.objects.all()
      
        serializer = CategorySerializer(category,many = True)

        return Response({'categories':serializer.data})
    

class UpdateCategory(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def put(self, request, pk):
        post = Category.objects.get(id=pk)
        serializer = CategorySerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "success": True, "message": "updated Category" })
        else:
            print(serializer.errors)
            return Response({ "success": False, "message": "error updating Category" })
        

class DestroyCategory(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            post = Category.objects.get(id=pk)
            
            self.perform_destroy(post)
            return Response({ "success": True, "message": "post deleted" })
            
        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })
        
