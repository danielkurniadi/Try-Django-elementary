from django.shortcuts import render
from .models import Product
from .forms import ProductModelForm

# Create your views here.
def product_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = Product()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=2)
    context={
        'object': obj,
    }
    return render(request, 'products/product_detail.html', context)