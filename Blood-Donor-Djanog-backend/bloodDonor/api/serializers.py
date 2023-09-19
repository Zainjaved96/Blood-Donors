from rest_framework import serializers
from .models import BloodDonor


class BloodDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonor
        fields = '__all__'  # You can specify specific fields here if needed
