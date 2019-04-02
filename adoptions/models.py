from django.db import models

class Adoption(models.Model):
    cat_id = models.ForeignKey('cats.Cat', on_delete=models.CASCADE, related_name='cats')
    adoption_first_name = models.CharField(max_length=255)
    adoption_last_name = models.CharField(max_length=255)
    adoption_address = models.CharField(max_length=255)
    adoption_city = models.CharField(max_length=255)
    adoption_state = models.CharField(max_length=255)
    adoption_zip = models.CharField(max_length=255)
    adoption_phone = models.CharField(max_length=255)
    adoption_email = models.CharField(max_length=255)
    adoption_housing = models.CharField(max_length=255)
    adoption_indoor_outdoor = models.CharField(max_length=255)
    adoption_move = models.CharField(max_length=255)
    adoption_why = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.adoption_last_name