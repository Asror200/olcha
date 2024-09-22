from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Group(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='group')
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='groups')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField()
    slug = models.SlugField(blank=True)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='products')

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Attribute(models.Model):
    attribute = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.attribute


class Value(models.Model):
    value = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.value


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_attributes')
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL, null=True, related_name='product_attributes')
    value = models.ForeignKey(Value, on_delete=models.SET_NULL, null=True,
                              related_name='product_attributes')

    def __str__(self):
        return f'{self.product}, {self.attribute}, {self.value}'


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_images')
    image = models.ImageField(upload_to='product', default=None)