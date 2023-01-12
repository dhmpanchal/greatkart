from django.db import models
from django.urls import reverse
from category.models import Category
from extras.models import BaseModel
from django.utils.html import mark_safe

# Create your models here.
class Product(BaseModel):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_products"
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('products_detail', args=[self.category.slug, self.slug])

    def image_tag(self):
        if self.images:
            return mark_safe('<img src="%s" width="70" height="70" />' % (self.images.url,))

    image_tag.short_description = 'Product Images'
    image_tag.allow_tags = True
