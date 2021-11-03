from rest_framework import serializers

from users.models import User
from .models import AssignRole, Rewad, Course, Student

from users.serializers import UserSerializer


class StudentsSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(write_only=True, source="course", queryset=Course.objects.all())
    class Meta:
        model = Student
        fields = "__all__"




class CoursesSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many=True, read_only = True)
    instructor = UserSerializer(read_only = True)   
    tas = UserSerializer(many = True, read_only = True)
    instructor_id = serializers.PrimaryKeyRelatedField(write_only=True, source="instructor", queryset=User.objects.all())

    class Meta:
        model = Course
        fields = '__all__'

class RewardsSerializer(serializers.ModelSerializer):
    owner = StudentsSerializer(read_only = True)
    owner_id = serializers.PrimaryKeyRelatedField(write_only=True, source = "owner",  queryset=Student.objects.all())
    class Meta:
        model = Rewad
        fields = "__all__"


class RolesSerializer(serializers.ModelSerializer):
    ta_name = UserSerializer(read_only=True)
    course = CoursesSerializer(read_only = True)
    ta_id = serializers.PrimaryKeyRelatedField(write_only=True, source = "ta_name",  queryset=User.objects.all())
    course_id = serializers.PrimaryKeyRelatedField(write_only=True, source = "course",  queryset=Course.objects.all())

    class Meta:
        model = AssignRole
        fields = "__all__"