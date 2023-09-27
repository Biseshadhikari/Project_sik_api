from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializer import *
from core.models import *

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view



class CreateCourse(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UpdateCourse(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CategorySerializer

    def put(self, request, pk):
        course = Course.objects.get(id=pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "success": True, "message": "updated Course" })
        else:
            print(serializer.errors)
            return Response({ "success": False, "message": "error updating Course" })

class DeleteCourse(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer   
    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            course = Course.objects.get(id=pk)

            bookmarks = Bookmark.objects.filter(choice = "course",saved_id = pk)

            
            self.perform_destroy(course)
            for bookmark in bookmarks:
                bookmark.delete()
            
            return Response({ "success": True, "message": "course deleted" })
            
        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "course does not exist" }) 

class RetrieveCourse(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request): 
        course = Course.objects.all()
      
        serializer = CourseSerializer(course,many = True)

        return Response({'courses':serializer.data})

class visitCourse(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # queryset = Course.objects.all()
    
    def get(self,request,pk):
        try:
            course = Course.objects.get(id = pk)
            print(course)
            
            serializer = CourseSerializers(course)
            return Response({"course": serializer.data })
            
            

        except:
            return Response({"error":"course not found"})

