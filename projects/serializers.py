from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ['project_name', 'project_cross_one','project_cross_two', 'project_address', 'project_city', 'project_state', 'project_zip', 'project_submitter', 'project_phone', 'project_email','project_description', 'project_status', 'created_at', 'updated_at']