from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(
            name='Moisturizers', slug='moisturizers')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'Moisturizers')


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='Moisturizers', slug='moisturizers')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1, product_name='Natural Moisturizing Factors + HA', slug='moisturizers', price='5.80', image='5.png')

    def test_products_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Natural Moisturizing Factors + HA')
