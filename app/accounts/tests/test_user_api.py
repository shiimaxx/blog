from rest_framework.test import APITestCase

from accounts.models import User


class UserApiTests(APITestCase):
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

    def test_user_list(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_method_not_allowd(self):
        dummy_user = {
            'username': 'dummy_user4',
            'qiita_id': 'dummy_qiita_user4'
        }

        response = self.client.post('/api/v1/users/', data=dummy_user)
        self.assertEqual(response.status_code, 405)

        response = self.client.put('/api/v1/users/{}/'.format(self.dummy_user1.id), data=dummy_user)
        self.assertEqual(response.status_code, 405)

        response = self.client.delete('/api/v1/users/{}/'.format(self.dummy_user1.id))
        self.assertEqual(response.status_code, 405)
