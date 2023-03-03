from django.urls import path, include, re_path
from . import views


from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
