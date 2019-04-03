from rest_framework import serializers
from .models import Adoption

class AdoptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Adoption
    fields = ['cat', 'adoption_first_name', 'adoption_last_name', 'adoption_address', 'adoption_city', 'adoption_state', 'adoption_zip', 'adoption_phone', 'adoption_email', 'adoption_housing', 'adoption_indoor_outdoor', 'adoption_move', 'adoption_move', 'adoption_why', 'created_at', 'updated_at']