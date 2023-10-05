from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts")

    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    date = models.DateTimeField()
    # location = models.location()
    # participant = models.ManyToManyField(User, blank=True, related_name='events')
    updated = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User,
                                   related_name='eventpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
