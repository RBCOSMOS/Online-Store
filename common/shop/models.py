from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    title = models.CharField(max_length = 255, db_index = True)
    info = models.TextField(blank = True)
    price = models.IntegerField()
    categories = models.ManyToManyField('Category', related_name = 'products')
    image = models.ImageField(upload_to = 'images/', default = 'images/default_img.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs = {'pk': self.pk})


class Category(models.Model):
    title = models.CharField(max_length = 150, db_index = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs = {'pk': self.pk})

class Order(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 150)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)

    def save_order(request):
        product_id = request.POST['product_id']
        order = Order()
        order.name = request.POST['name']
        order.email = request.POST['email']
        order.product = Product.objects.get(pk = product_id)
        order.save()
        return render(request, 'shop/save_order.html')

