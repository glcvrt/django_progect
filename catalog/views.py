from django.shortcuts import render

from catalog.models import Product


def home_page(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'catalog/home_page.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Подписки'
    }
    return render(request, 'catalog/products.html', context)
