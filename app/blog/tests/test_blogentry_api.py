from rest_framework.test import APITestCase

from datetime import datetime
import json
from pytz import timezone

from accounts.models import User
from blog.models import Category, BlogEntry


class BlogEntryApiTests(APITestCase):
    def setUp(self):
        self.dummy_user1 = User.objects.create(
            username='dummy_user1',
            qiita_id='dummy_qiita_user1'
        )
        self.dummy_user2 = User.objects.create(
            username='dummy_user2',
            qiita_id='dummy_qiita_user2'
        )
        self.dummy_user3 = User.objects.create(
            username='dummy_user3',
            qiita_id='dummy_qiita_user3'
        )

        self.dummy_category1 = Category.objects.create(
            name='dummy_category1'
        )
        self.dummy_category2 = Category.objects.create(
            name='dummy_category2'
        )

        def add_timezone(created_at):
            return created_at.astimezone(timezone('Asia/Tokyo'))

        BlogEntry.objects.create(
            id='dummy_id1',
            title='dummy_entry1',
            content='dummy_content1',
            created_at=add_timezone(datetime(2018, 1, 1, 0, 0)),
            category=self.dummy_category1,
            user=self.dummy_user1
        )
        BlogEntry.objects.create(
            id='dummy_id2',
            title='dummy_entry2',
            content='dummy_content2',
            created_at=add_timezone(datetime(2018, 1, 5, 10, 0)),
            category=self.dummy_category2,
            user=self.dummy_user1
        )
        BlogEntry.objects.create(
            id='dummy_id3',
            title='dummy_entry3',
            content='dummy_content3',
            created_at=add_timezone(datetime(2018, 2, 11, 7, 20)),
            category=self.dummy_category1,
            user=self.dummy_user2
        )
        BlogEntry.objects.create(
            id='dummy_id4',
            title='dummy_entry4',
            content='dummy_content4',
            created_at=add_timezone(datetime(2018, 2, 20, 14, 15)),
            category=self.dummy_category2,
            user=self.dummy_user2
        )

    def test_blog_entry_list(self):
        response = self.client.get('/api/v1/users/{}/blogentries/'.format(self.dummy_user1.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        response = self.client.get('/api/v1/users/{}/blogentries/'.format(self.dummy_user2.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        response = self.client.get('/api/v1/users/{}/blogentries/'.format(self.dummy_user3.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_method_not_allowd(self):
        entry = {
            'id': 'dummy_id5',
            'title': 'dummy_entry5',
            'content': 'dummy_content5',
            'created_at': '2018-03-01T00:00:00+09:00',
            'category': '{"name": "dummy_category1"}',
            'user': '{"id": "dummy_qiita_user1"}'
        }
        response = self.client.post('/api/v1/users/{}/blogentries/'.format(self.dummy_user1.id), data=entry)
        self.assertEqual(response.status_code, 405)

        response = self.client.put('/api/v1/users/{}/blogentries/'.format(self.dummy_user1.id), data=entry)
        self.assertEqual(response.status_code, 405)

        response = self.client.delete('/api/v1/users/{}/blogentries/dummy_id1/'.format(self.dummy_user1.id))
        self.assertEqual(response.status_code, 405)
