from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('courses/', views.CourseList.as_view(), name="course_list"),
    path('courses/new/', views.CourseCreate.as_view(), name="course_create"),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name="course_detail"),
]