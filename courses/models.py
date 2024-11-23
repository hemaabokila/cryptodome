from django.db import models
from slugify import slugify
import random

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='courses/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            while Course.objects.filter(slug=slug).exists():
                slug = f"{slug}-{random.randint(1, 1000)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/courses/course/{self.slug}/videos/"

class Video(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    desc = models.TextField(blank=True, null=True)
    python_code = models.TextField(blank=True, null=True)
    cpp_code = models.TextField(blank=True, null=True)
    dart_code = models.TextField(blank=True, null=True)
    bash_code = models.TextField(blank=True, null=True)
    json_data = models.JSONField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='courses/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    video_url = models.CharField(max_length=200)
    youtube_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            while Video.objects.filter(slug=slug).exists():
                slug = f"{slug}-{random.randint(1, 1000)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/courses/course/{self.course.slug}/video/{self.slug}/"
