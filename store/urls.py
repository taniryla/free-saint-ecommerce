from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),  # delete when store app created
    path('', views.store, name='store'),  # delete when store app created
    # path('store/', include('store.urls')),
    # delete when order/cart app created
    path('cart/', views.cart, name='cart'),
    # path('cart/', include('cart.urls')),
    # delete when search is created
    path('product_detail/', views.product_detail, name='product_detail'),
]
