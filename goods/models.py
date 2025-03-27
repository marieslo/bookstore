from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Category Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ("id",)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Book Title')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='Book Cover')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Price')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Discount (%)')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity Available')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Category')
    author = models.CharField(max_length=255, verbose_name='Author', default='Unknown Author')
    publisher = models.CharField(max_length=255, verbose_name='Publisher', default='Unknown Publisher')
    publication_date = models.DateField(verbose_name='Publication Date', default='Unknown Date')


    class Meta:
        db_table = 'product'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} - {self.author}'

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)
