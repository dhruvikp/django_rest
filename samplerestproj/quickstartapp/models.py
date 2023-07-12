from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    mobile_num = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name+" "+ self.last_name