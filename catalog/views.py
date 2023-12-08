from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.models import Product, Blog


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products.html'


def home_page(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'catalog/home_page.html', context)


# def contacts(request):
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contacts.html', context)


# def products(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'Подписки'
#     }
#     return render(request, 'catalog/products.html', context)

class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Blogs',
    }

    template_name = 'catalog/blog_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(is_published=True)
        return qs


class BlogCreateView(CreateView):
    model = Blog
    extra_context = {
        'title': 'Create post',
    }
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    extra_context = {
        'title': 'Update post',
    }
    fields = ['title', 'content', 'image', 'is_published']

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('slug')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
