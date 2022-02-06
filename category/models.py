from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=true)
    slug = models.CharField(max_length=100, unique=true)
    description = models.CharField(max_length=225, blank=true)
    cat_image = models.ImageField(upload='photos/categories', blank=true)

    def __str__(self):
        return self.category_name
