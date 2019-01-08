from django.shortcuts import render
from .models import Product
from .forms import ProductModelForm, RawProductForm

# Create your views here.

# def product_create_view(request):
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             # Now data is good
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             # Invalid form
#             print(form.errors)
#     else:
#         form = RawProductForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'products/product_create.html', context)

def render_initial_data(request):
    initial_data = {
        'title': "My title..."
    }
    obj = Product.objects.get(id=2)
    form = ProductModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)

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