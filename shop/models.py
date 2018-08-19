from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(max_length=200, blank=True)
    country = models.CharField(max_length=100, default='Дубаи')
    articul = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price2 = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(upload_to='products', blank=True)
    image2 = models.ImageField(upload_to='products', blank=True)
    image3 = models.ImageField(upload_to='products', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class Text(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    text1 = models.TextField(blank=True)
    text2 = models.TextField(blank=True)
    text3 = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Main(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=100, default='#')
    image = models.ImageField(upload_to='cards', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
