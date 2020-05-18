from django.db import models
import re


class Post(models.Model):
    title = models.TextField(max_length=100)
    body = models.TextField(max_length=25000)
    published_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return re.sub(r"<([/]*[a-z0-9]*)>", "", str(self.title))
