from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Person,Color
from myapp.serializers import PersonSerializer,ColorSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer