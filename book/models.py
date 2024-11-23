from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class BookFile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='books/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/books/"
    
