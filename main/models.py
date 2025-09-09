import uuid
from django.db import models

class Product(models.Model):
    # Pilihan kategori toko yang tersedia 
    CATEGORY_CHOICES = [ 
        ('jersey', 'Jersey'),
        ('sneakers', 'Sneakers'),
        ('shirts', 'Shirts'),
        ('gloves', 'Gloves'),
        ('shorts', 'Baggy Shorts')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

