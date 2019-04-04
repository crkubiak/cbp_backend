from django.contrib import admin # brings in the admin ability
from .models import Post # brings in your Post model from the models.py file

admin.site.register(Post) # registers Post with your admin ability