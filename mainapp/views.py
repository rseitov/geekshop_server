import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from mainapp.models import ProductCategory,Product
# Create your views here.

links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},

]

module_dir = os.path.dirname(__file__)

def index(request):
    return render(request, 'mainapp/index.html')

def products(request, pk=None):
    print(pk)
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    products = json.load(open(file_path, encoding='utf-8'))

    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'products': products
    }
    return render(request, 'mainapp/products.html', content)

def contact(request):
    return render(request, 'mainapp/contact.html')


def context(request):
    content = {
        'title': 'магазин',
        'header': 'Добро пожаловать на сайт',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Стулья', 'price': 4535 },
            {'name': 'Диваны', 'price': 1535 },
            {'name': 'Кровати', 'price': 2535 },
        ]
    }

    return render(request, 'mainapp/test_context.html', content)

def main(request):



     title = 'главная'

     products = Product.objects.all()[:3]

     content = {
        'title': title,
        'products':products
     }

     return render(request, 'mainapp/index.html', content)