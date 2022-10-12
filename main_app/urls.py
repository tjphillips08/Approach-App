from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('about/', views.About.as_view(), name="about"),
    path('courses/', views.CourseList.as_view(), name="course_list"),
    path('courses/new/', views.CourseCreate.as_view(), name="course_create"),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name="course_detail"),
    path('courses/<int:pk>/update', views.CourseUpdate.as_view(), name="course_update"),
    path('courses/<int:pk>/delete', views.CourseDelete.as_view(), name="course_delete"),
    path('courses/<int:pk>/members/new', views.MemberCreate.as_view(), name="member_create"),
    path('clubs/', views.ClubList.as_view(), name="club_list"),
    path('clubs/<int:pk>/members/<int:member_pk>/', views.ClubMemberAssoc.as_view(), name="club_member_assoc"),
    path('clubs/<int:pk>/', views.ClubDetail.as_view(), name="club_detail"),
    path('clubs/new/', views.ClubCreate.as_view(), name="club_create"),
    path('', views.PostList.as_view(), name="home"),
    path('posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
    
    
    
    
]