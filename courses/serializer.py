from rest_framework import serializers
from .models import Rewads, Courses, Students



class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ["id", "first_name", "last_name", "course"]


class CoursesSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many=True)   

    class Meta:
        model = Courses
        fields = '__all__'

class RewardsSerializer(serializers.ModelSerializer):
    owner = StudentsSerializer(read_only = True)
    owner_id = serializers.PrimaryKeyRelatedField(write_only=True, source = "owner",  queryset=Students.objects.all())
    class Meta:
        model = Rewads
        fields = "__all__"
