from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		
        "API Overview": "This is an overview of the API endpoints for managing categories, courses, lessons, videos, notes, Q&A, bookmarks, and user-related actions.",
        "User": {
            "Create User": "/user/create/ [POST] - Create a new user account.",
            "Login User": "/user/login/ [POST] - Log in an existing user.",
            "Retrieve User": "/users/ [GET] - Retrieve a list of users.",
			"Pending":"User detail view is yet to be added",
        },
        "Categories": {
            "Retrieve Categories": "/categories/ [GET] - Retrieve a list of categories.",
            "Create Category": "/category/create/ [POST] - Create a new category.",
            "Update Category": "/category/update/<int:pk>/ [PUT] - Update a category by ID.",
            "Delete Category": "/category/delete/<int:pk>/ [DELETE] - Delete a category by ID.",
        },
        "Courses": {
            "Create Course": "/course/create/ [POST] - Create a new course.",
            "Retrieve Course": "/courses/ [GET] - Retrieve a list of courses.",
            "Visit Course": "/course/<int:pk>/ [GET] - Retrieve course details by ID.",
            "Update Course": "/course/update/<int:pk>/ [PUT] - Update a course by ID.",
            "Delete Course": "/course/delete/<int:pk>/ [DELETE] - Delete a course by ID.",
        },
        "Lessons": {
            "Create Lesson": "/course/<int:pk>/create/lesson/ [POST] - Create a new lesson within a course.",
            "Create Lessons": "/lesson/create/ [POST] - Create multiple lessons.",
            "List Lessons": "/courses/<int:pk>/lessons/ [GET] - Retrieve lessons for a specific course.",
            "Visit Lesson": "/lesson/<int:pk>/ [GET] - Retrieve lesson details by ID.",
            "Update Lesson": "/lesson/update/<int:pk>/ [PUT] - Update a lesson by ID.",
            "Delete Lesson": "/lesson/delete/<int:pk>/ [DELETE] - Delete a lesson by ID.",
        },
        "Lesson Videos": {
            "Create Lesson Video": "/lessonVideo/create/ [POST] - Create a new lesson video.",
            "List Lesson Videos": "/lesson/<int:pk>/videos/ [GET] - Retrieve videos for a specific lesson.",
            "Visit Lesson Video": "/lessonvideo/<int:pk>/ [GET] - Retrieve video details by ID.",
            "Update Lesson Video": "/lessonvideo/update/<int:pk>/ [PUT] - Update a lesson video by ID.",
            "Delete Lesson Video": "/lessonvideo/delete/<int:pk>/ [DELETE] - Delete a lesson video by ID.",
        },
        "Notes & Q&A": {
            "Create Note": "/note/create/ [POST] - Create a new note.",
            "Update Note": "/note/update/<int:pk>/ [PUT] - Update a note by ID.",
            "Delete Note": "/note/delete/<int:pk>/ [DELETE] - Delete a note by ID.",
            "List Notes": "/lessonvideo/<int:pk>/note/ [GET] - Retrieve notes for a specific video.",
            "Create Q&A": "/QandA/create/ [POST] - Create new Q&A entries.",
            "Update Q&A": "/QandA/update/<int:pk>/ [PUT] - Update a Q&A entry by ID.",
            "Delete Q&A": "/QandA/delete/<int:pk>/ [DELETE] - Delete a Q&A entry by ID.",
        },
        "Bookmarks": {
            "Bookmark Item": "/bookmark/<str:choice>/<int:pk>/ [POST] - Bookmark an item by type and ID.",
            "List Bookmarks": "/bookmarks/ [GET] - Retrieve user bookmarks.",
            "Bookmarks Detail": "/bookmarks/<str:choice>/ [GET] - Retrieve bookmarks by type.",
            "Delete Bookmark": "/bookmarks/delete/<int:pk>/ [DELETE] - Delete a bookmark by ID.",
        },
		'Forgot Password-related endpoints': {
            'Send OTP': '/send-otp/ (email is the only field)',
            'Verify OTP and Reset Password': '/verify-otp/ (email,otp,newpassword are the fields)',
        },
		
		}

	return Response(api_urls)