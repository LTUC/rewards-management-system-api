from django.db import models

class Points(models.Model):
    PRIZES = {
        ("Waive Late Assignment Penalty","Waive Late Assignment Penalty"),
        ("Waive Late of class penalty","Waive Late of class penalty"),
        ("+1 mark on any submission","+1 mark on any submission"),
        ("Resubmit attempt","Resubmit attempt"),
    }
    owner = models.CharField(max_length=40)
    reward = models.CharField(choices=PRIZES, max_length=80)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner
