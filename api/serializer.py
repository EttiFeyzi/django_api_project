from dataclasses import fields
from accounts.models import MyUser
from products.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('image', 'title', 'description', 'price','created','recored', )



