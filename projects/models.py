from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_cross_one = models.CharField(max_length=255)
    project_cross_two = models.CharField(max_length=255)
    project_address = models.CharField(max_length=255)
    project_city = models.CharField(max_length=255)
    project_state = models.CharField(max_length=255)
    project_zip = models.CharField(max_length=255)
    project_submitter = models.CharField(max_length=255)
    project_phone = models.CharField(max_length=255)
    project_email = models.CharField(max_length=255)
    project_description = models.TextField()
    project_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.project_name