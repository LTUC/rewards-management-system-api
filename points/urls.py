from django.urls import path
from .views import CohortView, PointView, PointDetailsView

urlpatterns = [
    path('cohort/', CohortView.as_view(), name='cohort'),
    path('points/', PointView.as_view(), name='points'),
    path('points-details/<int:id>', PointDetailsView.as_view(), name='points-details'),
]