from django.db import models


class Cat(models.Model):
    cat_name = models.CharField(max_length=255)
    cat_age = models.CharField(max_length=2)
    cat_sex = models.CharField(max_length=10)
    cat_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.cat_name