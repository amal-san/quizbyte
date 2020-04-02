from django.urls import path ,include
from .views import *


urlpatterns = [
    path('list/',QuestionListView.as_view() ),
    path('home/',IndexView.as_view(),name='index'),
    path('subject/<int:pk>/',SubjectDetailView.as_view(),name='subject_detail'),
    path('subject/chapter/<int:pk>/',ChapterDetailView.as_view(),name='chapter_detail'),
    path('subject/chapter/question/<int:pk>/',QuestionDetailView.as_view(),name='question_detail'),
    path('access/',LoginView.as_view(),name='auth'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
]
