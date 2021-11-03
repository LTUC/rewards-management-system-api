from django.db import models
from users.models import User
# Create your models here.


class Course(models.Model):
    code = models.CharField(max_length=40, blank=False)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name="instructor")
    tas = models.ManyToManyField(User, through="AssignRole")

    def __str__(self) -> str:
        return self.code

class AssignRole(models.Model):
    ta_name = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    course = models.ForeignKey(Course, blank=False, on_delete=models.SET_NULL, related_name="students", null=True)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

class Rewad(models.Model):
    PRIZES = {
        ("Waive Late Assignment Penalty","Waive Late Assignment Penalty"),
        ("Waive Late of class penalty","Waive Late of class penalty"),
        ("+1 mark on any submission","+1 mark on any submission"),
        ("Resubmit attempt","Resubmit attempt"),
    }
    owner = models.ForeignKey(Student, blank=False, on_delete=models.CASCADE)
    reward = models.CharField(choices=PRIZES, max_length=80)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.owner.first_name} {self.owner.last_name}')
