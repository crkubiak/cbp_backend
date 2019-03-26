from rest_framework import serializers
from .models import Cat

class CatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cat
    fields = ['cat_name', 'cat_age', 'cat_sex', 'cat_description']