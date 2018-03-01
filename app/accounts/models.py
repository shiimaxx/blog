from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    qiita_id = models.CharField('Qiita ID', max_length=50, blank=True)
