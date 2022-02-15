from unittest import skip
from django.test import TestCase, Client
from django.contrib.auth.models import User
from store.models import Category, Product
from django.urls import reverse
from store.views import all_products
from django.http import HttpRequest

# simulate a user going through the view

# @skip
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


def test_homepage_url(self):
    """
    Test homepage response status
    """
    response = self.Client.get('/')


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name='Moisturizers', slug='moisturizers')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1, product_name='Natural Moisturizing Factors + HA', slug='moisturizers', price='5.80', image='5.png')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.c.get(
            reverse('store:product_detail', args=['moisturizers']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category respponse status
        """
        response = self.c.get(
            reverse('store:category_list', args=['moisturizers']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>CORS</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
