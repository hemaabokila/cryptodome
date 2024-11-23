from django.db import models
    
class Codes(models.Model):
    name= models.CharField(max_length=100)  
    description= models.TextField() 
    example=models.TextField(blank=True, null=True)
    install = models.CharField(max_length=100)
    url=models.URLField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    example = models.TextField()
    install = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    


