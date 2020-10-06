from . import views 
from django.urls import path
 
urlpatterns = [ 
    path('api/products/', views.product_list),
    path('api/products/add/', views.add_product),
    path('api/products/delete/', views.delete_all_products),
    path('api/products/<str:pk>', views.product_detail),
]