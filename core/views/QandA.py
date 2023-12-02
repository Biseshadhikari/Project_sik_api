from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from core.serializer import *
from core.models import *
from rest_framework.response import Response
class CreateQandA(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = QandA.objects.all()
    serializer_class = QandASerializer



class listQandA(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
        try : 
            course = Course.objects.get(id = pk)
            # print(lesson)
            qanda = QandA.objects.filter(course = course)
            # print(lessonvideo)
            serializer = QandASerializer(qanda, many=True)
            return Response({ "success": True, "QAndA": serializer.data })
        except:
            return Response({ 
                "error":"Related QandA not available"
            })   
        




class UpdateQandA(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = QandA.objects.all()
    serializer_class = QandASerializer

    def put(self, request, pk):
        qanda = QandA.objects.get(id=pk)
        serializer = QandASerializer(qanda, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "success": True, "message": "qanda updated" })
        else:
            print(serializer.errors)
            return Response({ "success": False, "message": "error updating QandA" })

class DeleteQandA(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = QandA.objects.all()
    serializer_class = QandASerializer   
    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            qanda = QandA.objects.get(id=pk)
            
            self.perform_destroy(qanda)
            return Response({ "success": True, "message": "qanda deleted" })
            
        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "qanda does not exist" }) 