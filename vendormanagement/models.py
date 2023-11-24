from django.db import models
from django.db.models import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def calculate_on_time_delivery_rate(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        total_completed_pos = completed_pos.count()
        if total_completed_pos > 0:
            on_time_deliveries = completed_pos.filter(delivery_date__lte=F('acknowledgment_date')).count()
            return on_time_deliveries / total_completed_pos
        else:
            return 0.0

    def calculate_quality_rating_avg(self):
        completed_pos = self.purchaseorder_set.filter(status='completed').exclude(quality_rating__isnull=True)
        return completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0

    def calculate_average_response_time(self):
        completed_pos = self.purchaseorder_set.filter(status='completed').exclude(acknowledgment_date__isnull=True)
        response_times = completed_pos.aggregate(Avg(F('acknowledgment_date') - F('issue_date')))['acknowledgment_date__avg']
        return response_times.total_seconds() / 3600 if response_times else 0.0

    def calculate_fulfillment_rate(self):
        total_pos = self.purchaseorder_set.count()
        if total_pos > 0:
            successfully_fulfilled_pos = self.purchaseorder_set.filter(status='completed', issues__isnull=True).count()
            return successfully_fulfilled_pos / total_pos
        else:
            return 0.0

    def update_performance_metrics(self):
        self.on_time_delivery_rate = self.calculate_on_time_delivery_rate()
        self.quality_rating_avg = self.calculate_quality_rating_avg()
        self.average_response_time = self.calculate_average_response_time()
        self.fulfillment_rate = self.calculate_fulfillment_rate()
        self.save()



class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO {self.po_number} - {self.vendor.name}"
        
    @receiver(post_save, sender='vendormanagement.PurchaseOrder')
    def update_vendor_metrics(sender, instance, **kwargs):
        if instance.status == 'completed':
            instance.vendor.update_performance_metrics()


    

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"