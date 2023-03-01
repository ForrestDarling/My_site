from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.



class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()#default="none")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Post(models.Model):
    slug = models.SlugField(unique=True, default="", null=False, blank=True)
    image = models.ImageField(upload_to="posts", null=True)#image_name = models.CharField(default="none", max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, 
                               null=True, related_name="posts")
    date = models.DateField(auto_now=True)#, default="")#auto_now=True)
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    content = models.TextField()#validators=[MinLengthValidator=(10)])    #CharField(max_length=500)
    tags = models.ManyToManyField(Tag)
    

    def __str__(self):
        return f"{self.title}: {self.author}"
        


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")