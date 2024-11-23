from django.db import models
    
class Tool(models.Model):
    name= models.CharField(max_length=100)  
    url=models.URLField()
    description= models.TextField() 
    image=models.ImageField(blank=True, null=True,upload_to='tools/')  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
