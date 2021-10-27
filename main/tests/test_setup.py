from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):

    def setUp(self) -> None:
        self.data_url = reverse('data')
        self.points_url = reverse('points')

        self.data_by_student = {
            "by_student":"Adham_Mhaydat",
        }

        self.point_data = {
            "owner":"Anas Abusaif",
            "reward": "+1 mark on any submission",
            "is_confirmed": False,
        }
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()