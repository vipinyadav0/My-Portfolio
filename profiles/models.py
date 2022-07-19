from django.db import models

# Create your models here
class Blog(models.Model):
    image = models.ImageField(upload_to = 'profiles/images')
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=600)

    def __str__(self):
        return self.title
    
class Resume(models.Model):
    resume = models.FileField(upload_to='profiles/data')
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=400)
    
    def __str__(self):
        return self.subject