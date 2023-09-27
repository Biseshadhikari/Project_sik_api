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





class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginUserView(APIView):

    def post(self, request):
        # request.data (email, password)
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data["email"])
                # print(user.is_admin)
                
                if user.check_password(serializer.validated_data["password"]):
                    token = Token.objects.get_or_create(user=user)
                    return Response({ "success": True, "token": token[0].key })
                else:
                    return Response({ "success": False, "message": "incorrect password" })
            except ObjectDoesNotExist:
                return Response({ "success": False, "message": "user does not exist" })
            


class RetrieveUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self,request): 
        user = User.objects.all()
        print(user
        )
        serializer = RetiveUserSerializer(user,many = True)
        # print(serializer)
        # for i in serializer.data:
        #     print(i)
       
        # serializer = serializers.pop('password')
        
        return Response({'user':serializer.data})
    
