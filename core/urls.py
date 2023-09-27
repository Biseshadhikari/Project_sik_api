
from django.urls import path
from core.views.user import *
from core.views.category import *
from core.views.course import *
from core.views.lessons import *
from core.views.lessonvideo import *
from core.views.bookmark import *
from core.views.notes import *
from core.views.QandA import *
from core.views.overview import apiOverview
urlpatterns = [
    path('',apiOverview),
    path('user/create/', CreateUser.as_view()),
    path('user/login/', LoginUserView.as_view()),
    path('users/', RetrieveUser.as_view()),

    path('categories/', RetrieveCategory.as_view()),
    path('category/create/', CreateCategory.as_view()),
    path('category/update/<int:pk>/', UpdateCategory.as_view()),
    path('category/delete/<int:pk>/', DestroyCategory.as_view()),

    path('course/create/', CreateCourse.as_view()),
    path('course/<int:pk>/', visitCourse.as_view()),
    path('courses/', RetrieveCourse.as_view()),
    path('course/update/<int:pk>/', UpdateCourse.as_view()),
    path('course/delete/<int:pk>/', DeleteCourse.as_view()),

    path('lesson/create/', Createlessons.as_view()),
    path('courses/<int:pk>/lessons/', listLessons.as_view()),
    path('lesson/<int:pk>/', visitLesson.as_view()),
     path('lesson/update/<int:pk>/', UpdateLesson.as_view()),
    path('lesson/delete/<int:pk>/', DeleteLesson.as_view()),

    path('lessonVideo/create/',CreatelessonVideo.as_view()),
    path('lesson/<int:pk>/videos/', listLessonvideo.as_view()),
    path('lessonvideo/<int:pk>/', visitLessonVideo.as_view()),
    path('lessonvideo/update/<int:pk>/', UpdateLessonvideo.as_view()),
    path('lessonvideo/delete/<int:pk>/', DeleteLessonvideo.as_view()),


    path('note/create/',CreateNotes.as_view()),
    path('note/update/<int:pk>/', UpdateNotes.as_view()),
    path('note/delete/<int:pk>/', Deletenote.as_view()),
    path('lessonvideo/<int:pk>/note/',listNotes.as_view()),


    path('QandA/create/',CreateQandA.as_view()),
    path('QandA/update/<int:pk>/', UpdateQandA.as_view()),
    path('QandA/delete/<int:pk>/', DeleteQandA.as_view()),
    
    
    path('bookmarks/<str:choice>/<int:pk>/',BookmarkItem.as_view()),
    path('bookmarks/',Bookmarks.as_view()),
    path('bookmarks/<str:choice>/',BookmarksDetail.as_view()),
    path('bookmark/delete/<int:pk>/',BookmarkDelete.as_view()),

    
    
    


]
