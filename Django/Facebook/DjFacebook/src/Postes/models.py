from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    tag = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')
    draft = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)