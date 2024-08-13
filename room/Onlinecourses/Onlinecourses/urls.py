from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('signup/', views.sign_up, name='Sign up'),
    path('modules/<int:module_id>/', views.module_detail, name='module_detail'),
    path('video/', views.video_django, name='video django'),
]
