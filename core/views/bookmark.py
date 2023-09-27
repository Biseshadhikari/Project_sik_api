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

                    return Response({'error':"already added to bookmark"})
                else:
                    bm = Bookmark(user = request.user,course = course,choice= choice,saved_id = pk)
                    bm.save()
                    return Response({'success':"added to bookmark"})
            else:
                return Response({'error':"course not found"})

        elif choice == "lesson":
            lesson = Lesson.objects.filter(id = pk).first()
            if lesson:
                bookmark =Bookmark.objects.filter(user = request.user,lesson = lesson,choice= choice,saved_id = pk).first()
                if bookmark:
                    return Response({'error':"already added to bookmark"})
                else:
                    bm = Bookmark(user = request.user,lesson = lesson,choice= choice,saved_id = pk)
                    bm.save()
                    return Response({'success':"added to bookmark"})
                    
            else:
                return Response({'error':"lesson not found"})
                
        elif choice == "video":
            lessonvideo = lessonVideo.objects.filter(id = pk).first()
            if lessonvideo:
                    
                bookmark =Bookmark.objects.filter(user = request.user, video= lessonvideo,choice= choice,saved_id = pk).first()
                if bookmark:
                    return Response({'error':"already added to bookmark"})
                else:
                    bm = Bookmark(user = request.user, video= lessonvideo,choice= choice,saved_id = pk)
                    bm.save()
                    return Response({'success':"added to bookmark"})
            else:
                return Response({'error':"video not found"})

        else:
            return Response({'error':"Noting found"})



class Bookmarks(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Bookmarkserializers

    def get(self, request):
        try : 
            bookmark = Bookmark.objects.filter(user = request.user)
            print(bookmark)
            
            serializer = self.serializer_class(bookmark, many=True)
            return Response({ "success": True, "Bookmarks": serializer.data })
        except:
            return Response({ 
                "error":"Related bookamrks not available"
            })
    
class BookmarksDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # def get_object(self, request,choice = None):
    #     try : 
    #         bookmark = Bookmark.objects.filter(user = request.user)
            
    #         serializer = Bookmarkserializers(bookmark, many=True)
    #         return Response({ "success": True, "Bookmarks": serializer.data })
    #     except:
    #         return Response({ 
    #             "error":"Related bookamrks not available"
    #         })
    def get(self,request,choice):
        try : 
            bookmark = Bookmark.objects.filter(user = request.user,choice= choice)
            
            serializer = Bookmarkserializers(bookmark, many=True)
            return Response({ "success": True, "Bookmarks": serializer.data })
        except:
            return Response({ 
                "error":"Related bookamrks not available"
            })

class BookmarkDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # def get_object(self, request,choice = None):
    #     try : 
    #         bookmark = Bookmark.objects.filter(user = request.user)
            
    #         serializer = Bookmarkserializers(bookmark, many=True)
    #         return Response({ "success": True, "Bookmarks": serializer.data })
    #     except:
    #         return Response({ 
    #             "error":"Related bookamrks not available"
    #         })
    def delete(self, request, *args, **kwargs):
        try : 
            
            bookmark = Bookmark.objects.get(user = request.user,id = kwargs['pk'])
            print(bookmark)
            
            bookmark.delete()
            return Response({ "success": True, "Bookmarks": "deleted" })
        except:
            return Response({ 
                "error":"Related bookamrks not available"
            })
        
