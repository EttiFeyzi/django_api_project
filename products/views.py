
from django.views import generic
from products.forms import ProductForm
# from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product

# Create your views here.

class ProductList(generic.ListView):
    # model = Product
    template_name = 'products/prodct_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(active=True)


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class ProductCreate(generic.CreateView):
    form_class = ProductForm
    template_name = 'products/product_create.html' 
    

    



    


