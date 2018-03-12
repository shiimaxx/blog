from django.test import TestCase

from datetime import datetime
from unittest.mock import MagicMock, patch

from accounts.models import User
from aggregator.models import QiitaEntry
from blog.management.commands.qiita import save_qiita_entries


class TestQiita(TestCase):

    @patch('blog.management.commands.qiita._fetch_qiita_entries')
    def test_save_qiita_entries(self, mock_fetch_qiita_entries):
        dummy_user1 = User.objects.create(
            username='dummy_user1',
            qiita_id='dummy_qiita_user1'
        )
        dummy_user2 = User.objects.create(
            username='dummy_user2',
            qiita_id='dummy_qiita_user2'
        )

        dummy_entry1 = MagicMock()
        dummy_entry1.id = 'dummy_id1'
        dummy_entry1.title = 'dummy_entry1'
        dummy_entry1.url = 'https://qiita.com/dummy_qiita_user1/item/dummy_entry1'
        dummy_entry1.created_at = datetime(2018, 1, 1, 0, 0)
        dummy_entry1.user.id = 'dummy_qiita_user1'

        dummy_entry2 = MagicMock()
        dummy_entry2.id = 'dummy_id2'
        dummy_entry2.title = 'dummy_entry2'
        dummy_entry2.url = 'https://qiita.com/dummy_qiita_user1/item/dummy_entry2'
        dummy_entry2.created_at = datetime(2018, 1, 5, 10, 0)
        dummy_entry2.user.id = 'dummy_qiita_user1'

        dummy_entry3 = MagicMock()
        dummy_entry3.id = 'dummy_id3'
        dummy_entry3.title = 'dummy_entry3'
        dummy_entry3.url = 'https://qiita.com/dummy_qiita_user2/item/dummy_entry3'
        dummy_entry3.created_at = datetime(2018, 1, 3, 8, 30)
        dummy_entry3.user.id = 'dummy_qiita_user2'

        mock_fetch_qiita_entries.return_value = (dummy_entry1, dummy_entry2, dummy_entry3)

        save_qiita_entries([dummy_user1, dummy_user2])

        dummy_user1_qiita_entries = QiitaEntry.objects.filter(user=dummy_user1)
        self.assertEqual('dummy_id1', dummy_user1_qiita_entry['id'])
        self.assertEqual('dummy_entry1', dummy_user1_qiita_entry['title'])
