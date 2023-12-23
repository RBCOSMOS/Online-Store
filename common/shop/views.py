from django.shortcuts import render
from .models import Product, Category, Order
from django.views.generic import ListView, DetailView
from .utilities import CategoryListMixin

class ProductListView(ListView, CategoryListMixin):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return self.model.objects.filter(title__icontains=search_query)
        return self.model.objects.all()


class ProductDetailView(DetailView, CategoryListMixin):
    model = Product

class CategoryDetailView(DetailView, CategoryListMixin):
    model = Category

def save_order(request):
    product_id = request.POST['product_id']
    order = Order()
    order.name = request.POST['name']
    order.email = request.POST['email']
    order.product = Product.objects.get(pk = product_id)
    order.save()
    return render(request, 'shop/save_order.html', context = {'username': order.name, 'product_title': order.product.title})

# def product_list(request ):
#     category_list = Category.objects.all()
#     search_query = request.GET.get('search', None)
#     if search_query:
#         product_list = Product.objects.filter(title__icontains=search_query)
#     else:
#         product_list = Product.objects.all()
#     return render( request, 'shop/product_list.html', context = {'product_list': product_list, 'category_list': category_list})

# def product_detail(request, pk):
#     category_list = Category.objects.all()
#     product = Product.objects.get(pk = pk)
#     return render(request, 'shop/product_detail.html', context = {'product': product, 'category_list': category_list})

# def category_detail(request, pk):
#     category_list = Category.objects.all()
#     category = Category.objects.get(pk = pk)
#     return render(request, 'shop/category_detail.html', context = {'category': category,'category_list': category_list})