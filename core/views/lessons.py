from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from core.serializer import *
from core.models import *
from rest_framework.response import Response

class Createlessons(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class CreateLesson(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]


    def post(self, request, pk):
        try:
            context = {
                "request": request,
            }
            course = Course.objects.get(id=pk)
            #  request.data["post"] = post
            #  PostComment.objects.create(post=post, user=request.user, comment_text=request.data["comment_text"])
            serializer = self.serializer_class(context=context, data=request.data)
            if serializer.is_valid():

                serializer.save(course=course)
                return Response({ "success": True, "message": "Lesson added" })
            else:
                print(serializer.errors)
                return Response({ "success": False, "message": "error adding a Lesson" })

        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "Course does not exist" })
    
class listLessons(generics.ListAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
        try : 
            course = Course.objects.get(id = pk)
            lessons = Lesson.objects.filter(course = course)
            serializer = self.serializer_class(lessons, many=True)
            return Response({ "success": True, "lessons": serializer.data })
        except:
            return Response({ 
                "error":"Related Course not available"
            })
        


class visitLesson(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # queryset = Course.objects.all()
    
    def get(self,request,pk):
        try:
            
            lesson = Lesson.objects.get(id = pk)
            # print(course)
            
            serializer = LessonSerializers(lesson)
            return Response({"Lesson": serializer.data })
            
            

        except:
            return Response({"error":"lesson not found"})



class UpdateLesson(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def put(self, request, pk):
        lesson = Lesson.objects.get(id=pk)
        serializer = LessonSerializer(lesson, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "success": True, "message": "updated lesson" })
        else:
            print(serializer.errors)
            return Response({ "success": False, "message": "error updating lesson" })

class DeleteLesson(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer   
    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            lesson = Lesson.objects.get(id=pk)
            
            self.perform_destroy(lesson)
            return Response({ "success": True, "message": "lesson deleted" })
            
        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "lesson does not exist" }) 


