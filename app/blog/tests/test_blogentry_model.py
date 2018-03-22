from datetime import datetime

from rest_framework.test import APITestCase
from pytz import timezone

from accounts.models import User
from blog.models import Category, BlogEntry


class BlogEntryModelTests(APITestCase):
    def test_is_empty(self):
        entry = BlogEntry.objects.all()
        self.assertEqual(entry.count(), 0)

    def test_is_not_empty(self):
        dummy_user1 = User.objects.create(
            username='dummy_user1',
        )
        dummy_category1 = Category.objects.create(
            name='dummy_category1'
        )
        BlogEntry.objects.create(
            title='dummy_entry1',
            content='dummy_content1',
            category=dummy_category1,
            created_at=datetime(2018, 1, 1, 0, 0).astimezone(timezone('Asia/Tokyo')),
            user=dummy_user1
        )
        entry = BlogEntry.objects.all()
        self.assertEqual(entry.count(), 1)
