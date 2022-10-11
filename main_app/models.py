from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 100)
    img = models.CharField(max_length = 250)
    address = models.CharField(max_length = 150)
    website = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Member(models.Model):
    name = models.CharField(max_length = 100)
    handicap = models.IntegerField(default=0)
    email = models.CharField(max_length = 100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return self.name



class Club(models.Model):
    name = models.CharField(max_length = 100)
    img = models.CharField(max_length = 250)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.name



