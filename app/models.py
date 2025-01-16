from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.timezone import now

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    # def __str__(self):
    #     return self.name

    def __str__(self):
        return f'{self.name} - {self.email}'
     





class Video(models.Model):
    title = models.CharField(max_length=100)
    video = EmbedVideoField(blank=True)  
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title 




class Partner_Company(models.Model):
    image = models.ImageField(upload_to='logo/')

    def __str__(self):
        return str(self.image.url) if self.image else 'No Image'
    


    
class Banner(models.Model):
    video_banner = models.FileField(upload_to='videos/')

    def __str__(self):
        return str(self.video_banner) 
    





class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=300)  
    date = models.DateField(default=now)       
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  

    text_one =  models.CharField(max_length=10000)
    text_two =  models.CharField(max_length=10000)
    text_three =  models.CharField(max_length=10000)
    text_four =  models.CharField(max_length=10000)
    text_five =  models.CharField(max_length=10000)
    text_six =  models.CharField(max_length=10000)
    text_seven =  models.CharField(max_length=10000)

    faqs_one = models.CharField(max_length=10000,blank=True, null=True)
    faqs_two = models.CharField(max_length=10000,blank=True, null=True)
    faqs_three = models.CharField(max_length=10000,blank=True, null=True)
    faqs_four = models.CharField(max_length=10000,blank=True, null=True)
    faqs_five = models.CharField(max_length=10000,blank=True, null=True)
    faqs_six = models.CharField(max_length=10000,blank=True, null=True)
    faqs_seven = models.CharField(max_length=10000,blank=True, null=True)

    faqs_one_answer = models.CharField(max_length=10000,blank=True, null=True)
    faqs_two_answer = models.CharField(max_length=10000,blank=True, null=True)
    faqs_three_answer = models.CharField(max_length=10000,blank=True, null=True)
    faqs_four_answer = models.CharField(max_length=10000,blank=True, null=True)
    faqs_five_answer = models.CharField(max_length=10000,blank=True, null=True)
    faqs_six_answer = models.CharField(max_length=10000,blank=True, null=True)
    faqs_seven_answer = models.CharField(max_length=10000,blank=True, null=True)

    
    def __str__(self):
        return self.title