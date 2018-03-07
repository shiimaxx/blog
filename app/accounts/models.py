from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    qiita_id = models.CharField(unique=True, max_length=128, null=True)

    @classmethod
    def find_qiita_user(cls):
        return cls.objects.filter(qiita_id__isnull=False)

    @classmethod
    def get_from_qiita_id(cls, qiita_id):
        return cls.objects.filter(qiita_id=qiita_id).first()
