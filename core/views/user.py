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





class CreateUser(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                
                user = User.objects.get(email=serializer.validated_data["email"])
                return Response({ "success": False, "message": "User with this email already exists." }, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                user = User.objects.create_user(
                    email=serializer.validated_data["email"],
                    username=serializer.validated_data["username"],
                    password=serializer.validated_data["password"]
                )
                
                return Response({ "success": True,})


class LoginUserView(APIView):

    def post(self, request):
        # request.data (email, password)
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            try:
                user = User.objects.get(email=serializer.validated_data["email"])
                # print(user.is_admin)
                print(user.is_admin )
                
                if user.check_password(serializer.validated_data["password"]):
                    token = Token.objects.get_or_create(user=user)
                    return Response({ "success": True, "token": token[0].key,"admin":user.is_admin  })
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
    


