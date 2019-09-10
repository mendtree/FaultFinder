from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    username = models.ForeignKey('accounts.User', on_delete=models.CASCADE,)
    body = models.TextField()

def __str__(self):
    return self.title
