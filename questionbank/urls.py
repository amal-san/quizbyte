from django.urls import path ,include
from .views import *


urlpatterns = [
    path('list/',QuestionListView.as_view() ),
    path('',IndexView.as_view(),name='index'),
]
