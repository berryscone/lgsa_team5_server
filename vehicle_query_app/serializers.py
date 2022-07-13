from rest_framework import serializers

from .models import VehicleDetail


class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetail
        fields = ['id', 'created', 'plate_number', 'status', 'reg_exp',
                  'owner', 'birth', 'address',
                  'year', 'make', 'model', 'color']
