from django.db import models

class Cat(models.Model):
    project_id = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='projects')
    cat_name = models.CharField(max_length=255)
    cat_age = models.CharField(max_length=255)
    cat_sex = models.CharField(max_length=255)
    cat_size = models.CharField(max_length=255)
    cat_color = models.CharField(max_length=255)
    cat_coat = models.CharField(max_length=255)
    cat_description = models.TextField()
    cat_fix_spay = models.CharField(max_length=255)
    cat_declawed = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.cat_name