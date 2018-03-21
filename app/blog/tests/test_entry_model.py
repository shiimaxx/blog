from datetime import datetime

from rest_framework.test import APITestCase
from pytz import timezone

from accounts.models import User
from blog.models import Category, Entry


class EntryModelTests(APITestCase):
    def test_is_empty(self):
        entry = Entry.objects.all()
        self.assertEqual(entry.count(), 0)

    def test_is_not_empty(self):
        dummy_user1 = User.objects.create(
            username='dummy_user1',
            qiita_id='dummy_qiita_user1'
        )
        dummy_category1 = Category.objects.create(
            name='dummy_category1'
        )
        Entry.objects.create(
            id='dummy_id1',
            title='dummy_entry1',
            body='dummy_body1',
            category=dummy_category1,
            created_at=datetime(2018, 1, 1, 0, 0).astimezone(timezone('Asia/Tokyo')),
            user=dummy_user1
        )
        entry = Entry.objects.all()
        self.assertEqual(entry.count(), 1)
