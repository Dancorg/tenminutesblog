from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=100)
    body = models.TextField(max_length=25000)
    published_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
