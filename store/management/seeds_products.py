from django.core.management.base import BaseCommand
from ..models import Product, Category
import requests
import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://sephora.p.rapidapi.com/products/"

HEADERS = {
    'x-rapidapi-host': "sephora.p.rapidapi.com",
    'x-rapidapi-key': os.environ['RAPIDAPI_KEY']
}


def get_products():
    querystring = {"categoryId": "cat150006",
                   "pageSize": "60", "currentPage": "1"}
    response = requests.get(
        f'{BASE_URL}list', headers=HEADERS, params=querystring).json()
    products = response["products"]
    return products


def product_detail(pId, skuId):
    querystring = {"productId": pId, "preferedSku": skuId}
    response = requests.get(f'{BASE_URL}detail',
                            headers=HEADERS, params=querystring).json()
    return response


def clear_data():
    Product.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in get_products():
            detail = product_detail(i["productId"], i["currentSku"]["skuId"])
            product = Product(
                product_name=detail["brand"]["displayName"],
                slug=detail["brand"]["displayName"],
                description=detail["quickLookDescription"],
                price=float(detail["currentSku"]["listPrice"][1:]),
                product_images=detail["currentSku"]["skuImages"]["image135"],
                stock=100,
                category=Category(name=detail["parentCategory"]["parentCategory"]["displayName"],
                                  slug=detail["parentCategory"]["parentCategory"]["displayName"])
            )
            product.save()
        # clear_data()
            # print(detail["parentCategory"]["displayName"])
        self.stdout.write(self.style.SUCCESS("Complete"))
