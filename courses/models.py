from django.db import models

# Create your models here.


class Courses(models.Model):
    code = models.CharField(max_length=40, blank=False)
    instructor = models.CharField(max_length=100, blank=False)
    tas = models.JSONField()

    def __str__(self) -> str:
        return self.code


class Students(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    course = models.ForeignKey(Courses, blank=False, on_delete=models.SET_NULL, related_name="course", null=True)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

class Rewads(models.Model):
    PRIZES = {
        ("Waive Late Assignment Penalty","Waive Late Assignment Penalty"),
        ("Waive Late of class penalty","Waive Late of class penalty"),
        ("+1 mark on any submission","+1 mark on any submission"),
        ("Resubmit attempt","Resubmit attempt"),
    }
    owner = models.ForeignKey(Students, blank=False, on_delete=models.CASCADE)
    reward = models.CharField(choices=PRIZES, max_length=80)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.owner.first_name} {self.owner.last_name}')
