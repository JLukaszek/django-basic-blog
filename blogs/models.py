from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """Model representing post made by user."""
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
