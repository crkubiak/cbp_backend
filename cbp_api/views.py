from .models import Cat
from .serializers import CatSerializer
from rest_framework import viewsets

class CatViewSet(viewsets.ModelViewSet):
  queryset = Cat.objects.all()
  serializer_class = CatSerializer