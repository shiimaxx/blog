from django.db import models
from accounts.models import User


# Create your models here.
class QiitaEntry(models.Model):
    rendered_body = models.TextField()
    body = models.TextField()
    comments_count = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=128)
    like_count = models.PositiveIntegerField()
    private = models.BooleanField()
    reactions_count = models.PositiveIntegerField()
    title = models.CharField(max_length=128)
    updated_at = models.DateTimeField()
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page_views_count = models.PositiveIntegerField()
