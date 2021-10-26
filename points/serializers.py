from rest_framework import serializers
from .models import Cohort, Point


class CohortSerializer(serializers.ModelSerializer):
    instructor = serializers.SerializerMethodField()

    class Meta:
        model = Cohort
        fields = ["name", "instructor"]

    def get_instructor(self, obj):
        return obj.instructor.username


class PointSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Point
        fields = [
            "id",
            "owner",
            "prize",
            "is_confirmed",
            "is_donated",
            "donated_from",
            "donated_to",
            "notes",
        ]

    def get_owner(self, obj):

        # import pdb
        # pdb.set_trace()

        return obj.owner.username
