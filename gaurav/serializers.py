from rest_framework import serializers
from gaurav.models import company

class companySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=company
        fields="__all__"