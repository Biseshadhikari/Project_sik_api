from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from core.managers import MyUserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username =  models.CharField(max_length=200,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='img/',blank = True)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    @property
    def lessons(self):
        return self.Course.all()


class Lesson(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='Course',null=True,blank=True)
    description = models.CharField(max_length=200,null = True,blank = True)
    def __str__(self):
        return self.title
    
    @property
    def lessonVideo(self):
        return self.lesson.all()

class lessonVideo(models.Model):
    Course = models.ForeignKey(Course,on_delete=models.CASCADE,null = True,blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name="lesson")
    title = models.CharField(max_length=200,blank = True,null = True)
    video_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    class Meta:
      get_latest_by = "created_at"
    
    def save(self,*args, **kwargs):
        self.Course = self.lesson.course
        super().save(*args, **kwargs)


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video  = models.ForeignKey(lessonVideo,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200) 


class QandA(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    video  = models.ForeignKey(lessonVideo,on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)


choice = (('course','course'),('lesson','lesson'),('video','video'))
class Bookmark(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null = True,blank=True)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,null = True,blank=True)
    video = models.ForeignKey(lessonVideo,on_delete=models.CASCADE,null = True,blank=True)
    saved_id = models.IntegerField(blank=True,null=True)
    choice = models.CharField(choices=choice,max_length=30)


class PasswordResetOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)





