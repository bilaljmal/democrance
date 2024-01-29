import datetime
import secrets

from rest_framework import serializers
from backend_api.models import Customers, InsurancePolicy


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        exclude = ['id', 'updated_at', 'created_at']


class InsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = '__all__'


class QuoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = ['customer','type','status']
        extra_kwargs = {'status': {'required': False},'type': {'required': False}}



