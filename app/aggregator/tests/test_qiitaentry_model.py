
from datetime import datetime

from rest_framework.test import APITestCase
from pytz import timezone

from accounts.models import User
from aggregator.models import QiitaEntry


class QiitaEntryModelTests(APITestCase):
    def test_is_empty(self):
        entry = QiitaEntry.objects.all()
        self.assertEqual(entry.count(), 0)

    def test_is_not_empty(self):
        dummy_user1 = User.objects.create(
            username='dummy_user1',
            qiita_id='dummy_qiita_user1'
        )
        QiitaEntry.objects.create(
            id='dummy_id1',
            title='dummy_entry1',
            url='https://qiita.com/dummy_qiita_user1/item/dummy_entry1',
            created_at=datetime(2018, 1, 1, 0, 0).astimezone(timezone('Asia/Tokyo')),
            user=dummy_user1
        )
        entry = QiitaEntry.objects.all()
        self.assertEqual(entry.count(), 1)
