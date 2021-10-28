from django.urls import path

from .views import *

urlpatterns = [
    path('courses/', CoursesListView.as_view(), name='CoursesListView'),
    path('courses/<int:pk>', CoursesDetailtView.as_view(), name='CoursesDetailtView'),
    path('rewards/', RewardsListView.as_view(), name='RewardsListView'),
    path('rewards/<int:pk>', RewardsDetailtView.as_view(), name='RewardsDetailtView'),
    path('students/', StudentsListView.as_view(), name='StudentsListView'),
    path('students/<int:pk>', StudentsDetailtView.as_view(), name='StudentsDetailtView'),
]