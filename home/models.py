from django.db import models
from slugify import slugify 
import uuid
from django.utils.html import escape

class Blog(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='Blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.title = escape(self.title)
        self.sub_title = escape(self.sub_title)
        self.description = escape(self.description)
        if not self.slug:
            slug = slugify(self.title)
            if Blog.objects.filter(slug=slug).exists():
                slug = f"{slug}-{uuid.uuid4().hex[:8]}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    class Meta:
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['created_at']),
        ]

class AppVisit(models.Model):
    app_name = models.CharField(max_length=255)
    date = models.DateField()
    visit_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('app_name', 'date')
