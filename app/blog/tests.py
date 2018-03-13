from django.test import TestCase

from datetime import datetime, timedelta
import json
from unittest.mock import Mock, patch

from accounts.models import User
from aggregator.models import QiitaEntry
from blog.management.commands.qiita import save_qiita_entries


def mocked_requests_get(*args):
    dummy_response = Mock()

    if args[0] == 'https://qiita.com/api/v2/users/dummy_qiita_user1/items':
        dummy_response.text = json.dumps([{
            'id': 'dummy_id1',
            'title': 'dummy_entry1',
            'url': 'https://qiita.com/dummy_qiita_user1/item/dummy_entry1',
            'created_at': '2018-01-01T00:00:00+09:00',
            'user': {'id': 'dummy_qiita_user1'}
        },
        {
            'id': 'dummy_id2',
            'title': 'dummy_entry2',
            'url': 'https://qiita.com/dummy_qiita_user1/item/dummy_entry2',
            'created_at': '2018-01-05T10:00:00+09:00',
            'user': {'id': 'dummy_qiita_user1'}
        },
        ])

    if args[0] == 'https://qiita.com/api/v2/users/dummy_qiita_user2/items':
        dummy_response.text = json.dumps([{
            'id': 'dummy_id3',
            'title': 'dummy_entry3',
            'url': 'https://qiita.com/dummy_qiita_user2/item/dummy_entry3',
            'created_at': '2018-02-11T07:20:00+09:00',
            'user': {'id': 'dummy_qiita_user2'}
        },
        {
            'id': 'dummy_id4',
            'title': 'dummy_entry4',
            'url': 'https://qiita.com/dummy_qiita_user2/item/dummy_entry4',
            'created_at': '2018-02-20T14:15:00+09:00',
            'user': {'id': 'dummy_qiita_user2'}
        },
        ])

    return dummy_response


class TestQiita(TestCase):

    @patch('blog.management.commands.qiita.requests')
    def test_save_qiita_entries(self, mock_requests):
        mock_requests.get.side_effect = mocked_requests_get

        dummy_user1 = User.objects.create(
            username='dummy_user1',
            qiita_id='dummy_qiita_user1'
        )
        dummy_user2 = User.objects.create(
            username='dummy_user2',
            qiita_id='dummy_qiita_user2'
        )

        save_qiita_entries([dummy_user1, dummy_user2])

        entries = list(QiitaEntry.objects.filter(user=dummy_user1))
        self.assertEqual('dummy_id1', entries[0].id)
        self.assertEqual('dummy_entry1', entries[0].title)
        self.assertEqual('https://qiita.com/dummy_qiita_user1/item/dummy_entry1', entries[0].url)
        self.assertEqual(datetime(2018, 1, 1, 0, 0), entries[0].created_at.replace(tzinfo=None) + timedelta(hours=9))
        self.assertEqual(dummy_user1, entries[0].user)

        self.assertEqual('dummy_id2', entries[1].id)
        self.assertEqual('dummy_entry2', entries[1].title)
        self.assertEqual('https://qiita.com/dummy_qiita_user1/item/dummy_entry2', entries[1].url)
        self.assertEqual(datetime(2018, 1, 5, 10, 0), entries[1].created_at.replace(tzinfo=None) + timedelta(hours=9))
        self.assertEqual(dummy_user1, entries[1].user)

        entries = list(QiitaEntry.objects.filter(user=dummy_user2))
        self.assertEqual('dummy_id3', entries[0].id)
        self.assertEqual('dummy_entry3', entries[0].title)
        self.assertEqual('https://qiita.com/dummy_qiita_user2/item/dummy_entry3', entries[0].url)
        self.assertEqual(datetime(2018, 2, 11, 7, 20), entries[0].created_at.replace(tzinfo=None) + timedelta(hours=9))
        self.assertEqual(dummy_user2, entries[0].user)

        self.assertEqual('dummy_id4', entries[1].id)
        self.assertEqual('dummy_entry4', entries[1].title)
        self.assertEqual('https://qiita.com/dummy_qiita_user2/item/dummy_entry4', entries[1].url)
        self.assertEqual(datetime(2018, 2, 20, 14, 15), entries[1].created_at.replace(tzinfo=None) + timedelta(hours=9))
        self.assertEqual(dummy_user2, entries[1].user)
