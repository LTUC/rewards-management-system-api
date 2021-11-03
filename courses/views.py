from rest_framework import generics
from django_filters import rest_framework as filters


from .models import AssignRole, Course, Rewad, Student
from .serializer import CoursesSerializer, RewardsSerializer, RolesSerializer, StudentsSerializer
from .filters import RewardsFilter
# Create your views here.


class CoursesListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer


class CoursesDetailtView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer


class RolesListView(generics.ListCreateAPIView):
    queryset = AssignRole.objects.all()
    serializer_class = RolesSerializer

class RolesDetaileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssignRole.objects.all()
    serializer_class = RolesSerializer


class RewardsListView(generics.ListCreateAPIView):
    queryset = Rewad.objects.all()
    serializer_class = RewardsSerializer
    filterset_class =  RewardsFilter
    filter_backends= [filters.DjangoFilterBackend]




class RewardsDetailtView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rewad.objects.all()
    serializer_class = RewardsSerializer



class StudentsListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer



class StudentsDetailtView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer