# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='products/')  # Requires Pillow library

#     def __str__(self):
#         return self.name
    
# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     category = models.CharField(max_length=100, blank=True, null=True)
#     image = models.ImageField(upload_to='products/')  # Make sure you have media settings configured

#     def __str__(self):
#         return self.name
from django.db import models
# from database import db

from django.conf import settings

class Contact:
    collection = settings.MONGO_DB["contacts"]  # Collection name in MongoDB

    @staticmethod
    def insert_contact(data):
        Contact.collection.insert_one(data)  # Save data to MongoDB


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='products/')  # Ensure media settings are configured
    recommended_products = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='recommended_for'
    )

    def __str__(self):
        return self.name


class Recommendation(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='separate_recommendations',
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('display_order', '-created_at')

    @property
    def is_standalone(self):
        return True

    def __str__(self):
        return self.name
    
#db_connection
# person_collection = db['person']    

# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     image_url = models.URLField(max_length=500, null=True, blank=True)  # Store image URL


