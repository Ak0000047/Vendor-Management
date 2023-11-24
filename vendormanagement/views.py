from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics,viewsets,mixins
from vendormanagement.models import Vendor, PurchaseOrder, HistoricalPerformance
from vendormanagement.serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer



class VendorCreationAPIView(generics.RetrieveUpdateDestroyAPIView, generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Vendor deleted successfully."})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        performance_data = {
            'on_time_delivery_rate': instance.on_time_delivery_rate,
            'quality_rating_avg': instance.quality_rating_avg,
            'average_response_time': instance.average_response_time,
            'fulfillment_rate': instance.fulfillment_rate,
        }
        return Response({'vendor_data': VendorSerializer(instance).data, 'performance_data': performance_data})





class PurchaseOrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def delete(self, request, *args, **kwargs):
        
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Purchase Order deleted successfully."})

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response


class HistoricalPerformanceDetailAPIView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer




class AcknowledgePurchaseOrderAPIView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    def perform_update(self, serializer):
        serializer.save(acknowledgment_date=timezone.now())