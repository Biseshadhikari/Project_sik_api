from rest_framework import serializers
from core.models import  *


# User Serliziers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','password']

    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    # password2 = serializers.CharField()
    def validate(self, data):
        user = User.objects.filter(username = data['username']).first()
        email = User.objects.filter(email = data['email']).first()
        if user:
            raise serializers.ValidationError({'error':'username already exist'})
        if email:
            raise serializers.ValidationError({'error':'email already exist'})
        return data

    def create(self, validated_data):

        user = User.objects.create(**validated_data)
        user.set_password(self.validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class RetiveUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    username = serializers.CharField()

# lesson video serilizer
class lessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = lessonVideo
        fields = '__all__'
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    def validate(self, data):
        # course = Course.objects.all(id = data['course'])
       try:
        lessonvideo = lessonVideo.objects.filter(lesson =data['lesson'],title = data['title']).first()
        if lessonvideo:
            raise serializers.ValidationError({'error':'lesson already exist'})
        # print(data['course'])
        return data
       except:
           raise serializers.ValidationError({'error':'error adding lessonVideo'})

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())   

class QandASerializer(serializers.ModelSerializer):
    class Meta:
        model = QandA
        fields = '__all__'
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
# lesson Serilizers
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    def validate(self, data):
        # course = Course.objects.all(id = data['course'])
        
        try:
            
            lesson = Lesson.objects.filter(course =data['course'],title = data['title']).first()
            if lesson:
                raise serializers.ValidationError({'error':'lesson already exist'})
            # print(data['course'])
            return data
        except:
            raise serializers.ValidationError({'error':'Error adding lesson'})


    


class LessonSerializers(serializers.ModelSerializer):
    lessonVideo = lessonVideoSerializer(many = True)
    class Meta:
        model = Lesson
        fields = ['title','course','lessonVideo','description']
    

# category serlizers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

# course serilizers
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course

        fields = '__all__'
   
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

class CourseSerializers(serializers.ModelSerializer):
    lessons = LessonSerializer(many = True)
    class Meta:
        model = Course
        # fields = ['title','description','image','category']
        fields = ('id','title','description','image','Category','lessons')
        # depth = 2
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())



# bookmark serilizer
class Bookmarkserializers(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        exclude = ('lesson','video')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


from .models import PasswordResetOTP

class PasswordResetOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordResetOTP
        fields = '__all__'