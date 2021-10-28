from rest_framework import generics
from django_filters import rest_framework as filters


from .models import Courses, Rewads, Students
from .serializer import CoursesSerializer, RewardsSerializer, StudentsSerializer
from .filters import RewardsFilter
# Create your views here.


class CoursesListView(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class CoursesDetailtView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class RewardsListView(generics.ListCreateAPIView):
    queryset = Rewads.objects.all()
    serializer_class = RewardsSerializer
    filterset_class =  RewardsFilter
    filter_backends= [filters.DjangoFilterBackend]




class RewardsDetailtView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rewads.objects.all()
    serializer_class = RewardsSerializer



class StudentsListView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer



class StudentsDetailtView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer