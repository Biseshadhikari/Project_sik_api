from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from core.serializer import *
from core.models import *
from rest_framework.response import Response
class CreateNotes(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class listNotes(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
        try : 
            video = lessonVideo.objects.get(id = pk)
            # print(lesson)
            note = Notes.objects.filter(video = video)
            # print(lessonvideo)
            serializer = NotesSerializer(note, many=True)
            return Response({ "success": True, "note": serializer.data })
        except:
            return Response({ 
                "error":"Related note not available"
            })
        

class UpdateNotes(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

    def put(self, request, pk):
        notes = Notes.objects.get(id=pk)
        serializer = NotesSerializer(notes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "success": True, "message": "note updated" })
        else:
            print(serializer.errors)
            return Response({ "success": False, "message": "error updating note" })

class Deletenote(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer   
    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            note = Notes.objects.get(id=pk)
            
            self.perform_destroy(note)
            return Response({ "success": True, "message": "note deleted" })
            
        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "note does not exist" })        