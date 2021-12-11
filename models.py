from django.db import models
# from django.utils import timezone
# Create your models here.


class MvnsCollectedData(models.Model):
    orderNumber = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='orderNumber')
    dateDataCollected = models.DateField(auto_now_add=True, verbose_name='dateDataCollected')
    timeDataCollected = models.TimeField(auto_now_add=True, verbose_name='timeDataCollected')
    # use default=timezone.now if needed to edit (import timezone from django.utils)
    # use auto_now=True for last modified
    # use auto_now_add=True for exact time object was created but non-editable
    officerName = models.CharField(max_length=100, verbose_name='officerName')
    motoristFirstName = models.CharField(max_length=50, verbose_name='motoristFirstName')
    motoristMiddleInitial = models.CharField(max_length=3, verbose_name='motoristMiddleInitial', blank=True)
    motoristLastName = models.CharField(max_length=50, verbose_name='motoristLastName')
    plateNumber = models.CharField(max_length=10, verbose_name='plateNumber')
    dbReading = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='dbReading')
    distance = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='distance')
