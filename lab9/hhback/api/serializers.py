from rest_framework import serializers
from .models import Product, Category

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = 'all'

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = 'all'