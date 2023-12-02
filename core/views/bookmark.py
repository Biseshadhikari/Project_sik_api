from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializer import *
from core.models import *

from rest_framework.response import Response

class BookmarkItem(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Bookmarkserializers

    def post(self, request,choice,pk):
        context = {
            "request":request
        }
        if choice == "course":
            course = Course.objects.filter(id = pk).first()
            if course:
                bookmark = Bookmark.objects.filter(user = request.user,course = course,choice= choice,saved_id = pk).first()
                if bookmark:
                    bookmark.delete()
                    return Response({'message':"bookmark removed","bookmarked":False})
                else:
                    bm = Bookmark(user = request.user,course = course,choice= choice,saved_id = pk)
                    bm.save()
                    bmcheck = BookMarkCheck(user = request.user,course = course,types = choice,isBookmarked = True,bookmark = bm)
                    bmcheck.save()
                    return Response({'message':"added to bookmark","bookmarked":False})
            else:
                return Response({'message':"course not found"})

        elif choice == "lesson":
            lesson = Lesson.objects.filter(id = pk).first()
            if lesson:
                bookmark =Bookmark.objects.filter(user = request.user,lesson = lesson,choice= choice,saved_id = pk).first()
                if bookmark:
                    bookmark.delete()
                    return Response({'message':"bookmark removed","bookmarked":False})
                else:
                    bm = Bookmark(user = request.user,lesson = lesson,choice= choice,saved_id = pk)
                    bm.save()
                    bmcheck = BookMarkCheck(user = request.user,lesson = lesson,types = choice,isBookmarked = True,bookmark = bm)
                    bmcheck.save()
                    
                    return Response({'message':"added to bookmark","bookmarked":False})
                    
            else:
                return Response({'message':"lesson not found"})
                
        elif choice == "video":
            lessonvideo = lessonVideo.objects.filter(id = pk).first()
            if lessonvideo:
                    
                bookmark =Bookmark.objects.filter(user = request.user, video= lessonvideo,choice= choice,saved_id = pk).first()
                if bookmark:
                    bookmark.delete()
                    return Response({'message':"bookmark removed","bookmarked":False})
                else:
                    bm = Bookmark(user = request.user, video= lessonvideo,choice= choice,saved_id = pk)
                    bm.save()
                    return Response({'message':"added to bookmark","bookmarked":False})
            else:
                return Response({'message':"video not found"})

        else:
            return Response({'message':"Noting found"})



class Bookmarks(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Bookmarkserializers

    def get(self, request):
        try : 
            bookmark = Bookmark.objects.filter(user = request.user)
            print(bookmark)
            
            serializer = self.serializer_class(bookmark, many=True)
            return Response({ "message": True, "Bookmarks": serializer.data })
        except:
            return Response({ 
                "message":"Related bookamrks not available"
            })
    
class BookmarksDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # def get_object(self, request,choice = None):
    #     try : 
    #         bookmark = Bookmark.objects.filter(user = request.user)
            
    #         serializer = Bookmarkserializers(bookmark, many=True)
    #         return Response({ "message": True, "Bookmarks": serializer.data })
    #     except:
    #         return Response({ 
    #             "message":"Related bookamrks not available"
    #         })
    def get(self,request,choice):
        try : 
            bookmark = Bookmark.objects.filter(user = request.user,choice= choice)
            
            serializer = Bookmarkserializers(bookmark, many=True)
            return Response({ "message": True, "Bookmarks": serializer.data })
        except:
            return Response({ 
                "message":"Related bookamrks not available"
            })

class BookmarkDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # def get_object(self, request,choice = None):
    #     try : 
    #         bookmark = Bookmark.objects.filter(user = request.user)
            
    #         serializer = Bookmarkserializers(bookmark, many=True)
    #         return Response({ "message": True, "Bookmarks": serializer.data })
    #     except:
    #         return Response({ 
    #             "message":"Related bookamrks not available"
    #         })
    def delete(self, request, *args, **kwargs):
        try : 
            
            bookmark = Bookmark.objects.get(user = request.user,id = kwargs['pk'])
            print(bookmark)
            
            bookmark.delete()
            return Response({ "message": True, "Bookmarks": "deleted" })
        except:
            return Response({ 
                "message":"Related bookamrks not available"
            })
        

class BookmarkDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,choice,pk):
        try : 
            if choice =="course":
                course = Course.objects.get(id = pk)
                # print(course)
                bookmark = Bookmark.objects.filter(course = course,user = request.user,choice = choice).first()
                print(bookmark)
                serializer = Bookmarkserializers(bookmark )
                if bookmark:
                    return Response({ "message": True, "Bookmarks_Detail": serializer.data,"bookmarked":True })
                else:
                    return Response({ "message": True, "Bookmarks_Detail": serializer.data,"bookmarked":False })
            elif choice == "lesson":
                lesson = Lesson.objects.get(id = pk)
                # print(course)
                bookmark = Bookmark.objects.filter(lesson = lesson,user = request.user,choice = choice).first()
                print(bookmark)
                serializer = Bookmarkserializers(bookmark)
                if bookmark:
                    return Response({ "message": True, "Bookmarks_Detail": serializer.data,"bookmarked":True })
                else:
                    return Response({ "message": True, "Bookmarks_Detail": serializer.data,"bookmarked":False })
            



        except:
            return Response({ 
                "message":"Related bookamrks not available",
                "bookmarked":False
            })
