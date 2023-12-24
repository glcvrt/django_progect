from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products.html'


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


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
