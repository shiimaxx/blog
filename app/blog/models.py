from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class BlogEntry(models.Model):
    created_at = models.DateTimeField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
