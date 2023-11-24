from rest_framework import serializers
from vendormanagement.models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        vendor=serializers.CharField(read_only=True)
        model = PurchaseOrder
        fields = '__all__'

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        vendor=serializers.CharField(read_only=True)
        model = HistoricalPerformance
        fields = '__all__'