# from django.db.models.signals import post_delete
# from .models import *
# from django.dispatch import receiver


# @receiver(post_delete,sender = Course)
# def post_delete_course(sender,instance,**kwargs):
#     bookmarks = Bookmark.objects.filter(saved_id = instance.id,choice = "course")
#     for bookmark in bookmarks:
#         bookmark.delete()

    
# @receiver(post_delete,sender = Lesson)
# def post_delete_lesson(sender,instance,**kwargs):
#     bookmarks = Bookmark.objects.filter(saved_id = instance.id,choice = "lesson")
#     for bookmark in bookmarks:
#         bookmark.delete()    

# @receiver(post_delete,sender = lessonVideo)
# def post_delete_course(sender,instance,**kwargs):
#     bookmarks = Bookmark.objects.filter(saved_id = instance.id,choice = "video")
#     for bookmark in bookmarks:
#         bookmark.delete()         