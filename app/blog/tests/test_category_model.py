from rest_framework.test import APITestCase

from blog.models import Category


class CategoryModelTests(APITestCase):
    def test_is_empty(self):
        category = Category.objects.all()
        self.assertEqual(category.count(), 0)

    def test_is_not_empty(self):
        Category.objects.create(
            name='dummy_category1'
        )
        category = Category.objects.all()
        self.assertEqual(category.count(), 1)
