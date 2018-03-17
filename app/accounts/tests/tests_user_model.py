from rest_framework.test import APITestCase

from accounts.models import User


class UserModelTests(APITestCase):
    def test_is_empty(self):
        user = User.objects.all()
        self.assertEqual(user.count(), 0)

    def test_is_not_empty(self):
        User.objects.create(
            username='dummy_user1',
            qiita_id='dummy_qiita_user1'
        )
        user = User.objects.all()
        self.assertEqual(user.count(), 1)
