from django.urls import path
from .views import (product_create_view, 
    render_initial_data, dynamic_lookup_view, product_delete, product_list_view)


app_name = 'products'
urlpatterns = [
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('', product_list_view, name='product-list'),
    # path('delete/<int:id>/', product_delete, name='product-delete'),
    # path('create/', render_initial_data, name='product-create'),
    
]
    