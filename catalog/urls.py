from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home_page, ProductsListView, BlogListView, BlogCreateView, BlogUpdateView, \
    BlogDetailView, BlogDeleteView

# from catalog.views import products

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home_page'),
    # path('contacts/', contacts, name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('view/<slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('update/<slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<slug>/', BlogDeleteView.as_view(), name='blog_delete'),
]
