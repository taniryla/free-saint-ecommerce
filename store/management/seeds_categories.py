from django.core.management.base import BaseCommand
from ..models import Category
import requests

categories = [
    'Skincare',
    'Moisturizers',
    'Face',
    'Treatments',
    'Body Moisturizers',
    'Cleansers',
    'Lip',
    'Sunscreen',
    'Self Tanners',
    'Eye Care',
    'Masks',
    'Hair Styling & Treatments',
    'Women',
    'High Tech Tools'
]


def clear_data():
    Category.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # for i in categories:
        #     category = Category(
        #         name = i,
        #         slug = i
        #     )
        #     category.save()
        clear_data()
        self.stdout.write(self.style.SUCCESS("Complete"))
