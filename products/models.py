from distutils.command.upload import upload
from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    image = models.ImageField(upload_to ='image/', blank=True)
    title = models.CharField(max_length=100)
    recored = models.FileField(upload_to='recored/', blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

        
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.id])
    