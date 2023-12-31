from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="placeholder")

    def __str__(self):
        return slugify(self.name)

    def get_absolute_url(self):
        return reverse("home")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default="entertainment"
    )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_posts"
    )

    description = models.TextField()
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    venue = models.CharField(max_length=150)
    participants = models.ManyToManyField(
        User, blank=True, related_name="events")
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    registeration_deadline = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="eventpost_like", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
