from django.http import response
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Course, Student, Rewad

class TestCourseAppModels(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        test_student = Student.objects.create(first_name="Ahmad", last_name="Almohammad", course=test_course)
        test_student.save()

        test_rewards = Rewad.objects.create(owner=test_student, reward="+1 mark on any submission")
        test_rewards.save()


    def test_course_model(self):
        course = Course.objects.get(id=1)
        expected_code = f"{course.code}"
        expected_instructor = f"{course.instructor}"
        expected_tas = course.tas

        self.assertEqual(expected_code, "amman-python-401d2")
        self.assertEqual(expected_instructor, "Ahmad Alawad")
        self.assertEqual(expected_tas, {"tas": ["Saleh", "Bashar"]})
        self.assertEqual(str(course), "amman-python-401d2")

    def test_student_model(self):
        student = Student.objects.get(id=1)
        expected_first_name = f"{student.first_name}"
        expected_last_name = f"{student.last_name}"
        expected_course = f"{student.course.code}"

        self.assertEqual(expected_first_name, "Ahmad")
        self.assertEqual(expected_last_name, "Almohammad")
        self.assertEqual(expected_course, "amman-python-401d2")
        self.assertEqual(str(student), "Ahmad Almohammad")

    def test_reward_model(self):
        reward = Rewad.objects.get(id=1)
        expected_owner = str(reward.owner)
        expected_prize = f"{reward.reward}"

        self.assertEqual(expected_owner,"Ahmad Almohammad")
        self.assertEqual(expected_prize,"+1 mark on any submission")
        self.assertEqual(str(reward),"Ahmad Almohammad")



        
class TestCoursesEndPoints(APITestCase):
    def test_courses_list(self):

        response = self.client.get(reverse("CoursesListView"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_detail(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        response = self.client.get(reverse("CoursesDetailtView", args=[1]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data , {
            'id':1,
            'code': test_course.code,
            'instructor' : test_course.instructor,
            'tas': test_course.tas,
            'students':[]

        })

    def test_course_create(self):
        url = reverse("CoursesListView")

        data={
            "code" : "amman-python-d2",
            "instructor" : "Ahmad Alawad",
            "tas":{"tas": ["Saleh", "Bashar"]}
        }

        response = self.client.post(url,data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.get().code, "amman-python-d2")
        self.assertEqual(Course.objects.count(), 1)
     
    def test_course_update(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        url = reverse("CoursesDetailtView", args=[test_course.id])

        data = {
            "code" : "amman-python-401d2",
        }

        response = self.client.patch(url,data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.get().code , "amman-python-401d2")


    def test_course_delete(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        url = reverse("CoursesDetailtView", args=[test_course.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)




class TestStudentsEndPoints(APITestCase):
    def test_students_list(self):

        response = self.client.get(reverse("StudentsListView"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_students_detail(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        test_student = Student.objects.create(first_name="Ahmad", last_name= "Almohammad", course = test_course )
        test_student.save()


        response = self.client.get(reverse("StudentsDetailtView", args=[1]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data , {
            'id':1,
            'first_name': test_student.first_name,
            'last_name' : test_student.last_name,
            'course': test_course.id,

        })

    def test_students_create(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()
        url = reverse("StudentsListView")

        data={
            "first_name" : "Ahmad",
            "last_name" : "Almohammad",
            "course_id": test_course.id
        }

        response = self.client.post(url,data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.get().first_name, "Ahmad")
        self.assertEqual(Student.objects.count(), 1)


     
    def test_students_update(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        test_student = Student.objects.create(first_name="Ahmad", last_name="Almohammad", course=test_course)
        test_student.save()

        url = reverse("StudentsDetailtView", args=[test_student.id])

        data = {
            "first_name" : "Hadi",
        }

        response = self.client.patch(url,data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.get().first_name , "Hadi")


    def test_students_delete(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        test_student = Student.objects.create(first_name="Ahmad", last_name="Almohammad", course=test_course)
        test_student.save()

        url = reverse("StudentsDetailtView", args=[test_student.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)










class TestRewardsEndPoints(APITestCase):
    def test_rewards_list(self):

        response = self.client.get(reverse("RewardsListView"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rewards_detail(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        test_student = Student.objects.create(first_name="Ahmad", last_name= "Almohammad", course = test_course )
        test_student.save()

        test_rewards = Rewad.objects.create(owner=test_student, reward="+1 mark on any submission")
        test_rewards.save()


        response = self.client.get(reverse("RewardsDetailtView", args=[1]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_rewards_create(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        test_student = Student.objects.create(first_name="Ahmad", last_name= "Almohammad", course = test_course )
        test_student.save()
        url = reverse("RewardsListView")

        data={
            "owner_id" : test_student.id,
            "reward" : "+1 mark on any submission"
        }

        response = self.client.post(url,data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rewad.objects.get().owner.first_name, "Ahmad")
        self.assertEqual(Rewad.objects.count(), 1)


     
    def test_rewards_update(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        test_student = Student.objects.create(first_name="Ahmad", last_name="Almohammad", course=test_course)
        test_student.save()

        test_rewards = Rewad.objects.create(owner=test_student, reward="+1 mark on any submission")
        test_rewards.save()

        url = reverse("RewardsDetailtView", args=[test_rewards.id])

        data = {
            "reward" : "Resubmit attempt",
        }

        response = self.client.patch(url,data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Rewad.objects.get().reward , "Resubmit attempt")


    def test_students_delete(self):
        test_course = Course.objects.create(code="amman-python-401d2", instructor= "Ahmad Alawad", tas={"tas": ["Saleh", "Bashar"]} )
        test_course.save()

        test_student = Student.objects.create(first_name="Ahmad", last_name="Almohammad", course=test_course)
        test_student.save()

        test_rewards = Rewad.objects.create(owner=test_student, reward="+1 mark on any submission")
        test_rewards.save()

        url = reverse("RewardsDetailtView", args=[test_rewards.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)