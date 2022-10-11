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



class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body,self.name)