from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.student_login, name='student_login'),
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('vote/<int:candidate_id>/',
     views.vote_candidate,
     name='vote_candidate'),
]