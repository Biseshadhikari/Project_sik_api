from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from core.serializer import *
from core.models import *
from rest_framework.response import Response


class CreatelessonVideo(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = lessonVideo.objects.all()
    serializer_class = lessonVideoSerializer 


class listLessonvideo(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
        try : 
            lesson = Lesson.objects.get(id = pk)
            # print(lesson)
            lessonvideo = lessonVideo.objects.filter(lesson = lesson)
            # print(lessonvideo)
            serializer = lessonVideoSerializer(lessonvideo, many=True)
            return Response({ "success": True, "videos": serializer.data })
        except:
            return Response({ 
                "error":"Related video not available"
            })



class visitLessonVideo(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # queryset = Course.objects.all()
    
    def get(self,request,pk):
        try:
            
            lessonvideo = lessonVideo.objects.get(id = pk)
            # print(course)
            
            serializer = lessonVideoSerializer(lessonvideo)
            return Response({"Lesson_video": serializer.data })
            
            

        except:
            return Response({"error":"lesson not found"})
        



class UpdateLessonvideo(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = lessonVideo.objects.all()
    serializer_class = lessonVideoSerializer

    def put(self, request, pk):
        lessonvideo = lessonVideo.objects.get(id=pk)
        serializer = lessonVideoSerializer(lessonvideo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "success": True, "message": "updated lessonvideo" })
        else:
            print(serializer.errors)
            return Response({ "success": False, "message": "error updating lessonvideo" })

class DeleteLessonvideo(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = lessonVideo.objects.all()
    serializer_class = lessonVideoSerializer   
    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            lessonvideo = lessonVideo.objects.get(id=pk)
            
            self.perform_destroy(lessonvideo)
            return Response({ "success": True, "message": "lessonvideo deleted" })
            
        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "lessonvideo does not exist" })        