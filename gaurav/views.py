from django.shortcuts import render
from rest_framework import viewsets
from gaurav.models import company
from gaurav.serializers import companySerializer

# Create your views here.
class companyViewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companySerializer
