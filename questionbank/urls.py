from django.urls import path ,include
from .views import *


urlpatterns = [
    path('list/',QuestionListView.as_view() ),
    path('',IndexView.as_view(),name='index'),
    path('subject/<int:pk>',SubjectDetailView.as_view(),name='subject_detail'),
    path('chapter/<int:pk>/',ChapterDetailView.as_view(),name='chapter_detail'),
    path('question/<int:pk>/',QuestionDetailView.as_view(),name='question_detail'),
    path('access/',LoginView.as_view(),name='auth'),
    path('logout/',LogoutView.as_view(),name='logout'),

]
