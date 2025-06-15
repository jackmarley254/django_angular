from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# This code sets up the URL routing for the books API in a Django application.
# It uses Django REST Framework's DefaultRouter to automatically generate the URL patterns for the BookViewSet.
