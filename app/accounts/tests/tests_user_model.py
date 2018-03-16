from rest_framework.test import APITestCase

from accounts.models import User


class UserModelTests(APITestCase):
    def test_is_empty(self):
        entry = User.objects.all()
        self.assertEqual(entry.count(), 0)

    def test_is_not_empty(self):
        dummy_user1 = User.objects.create(
            username='dummy_user1',
            qiita_id='dummy_qiita_user1'
        )
        entry = User.objects.all()
        self.assertEqual(entry.count(), 1)
