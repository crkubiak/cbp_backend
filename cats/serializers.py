from rest_framework import serializers
from .models import Cat

class CatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cat
    fields = ['project','cat_name', 'cat_age', 'cat_sex', 'cat_size', 'cat_color', 'cat_coat', 'cat_description', 'cat_fix_spay', 'cat_declawed', 'created_at', 'updated_at']

    # test