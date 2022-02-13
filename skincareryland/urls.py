from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    # delete when category app created
    path('category/', views.category, name='category'),
]
