from django.urls import path

from .views import *

urlpatterns = [
    path('users/', UserListView.as_view(), name='UserListView' ),
    path('users/create/', UserCreateView.as_view(), name='UserCreateView' ),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='UserDetailsView'),
]