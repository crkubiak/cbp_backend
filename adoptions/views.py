from .models import Adoption
from .serializers import AdoptionSerializer
from rest_framework import viewsets

class AdoptionViewSet(viewsets.ModelViewSet):
  queryset = Adoption.objects.all()
  serializer_class = AdoptionSerializer