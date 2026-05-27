from django.db import models
from django.utils import timezone
from datetime import timedelta


class Batch(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    timing = models.CharField(max_length=100, null=True, blank=True)
    monthly_fee = models.IntegerField(null=True, blank=True)
    max_students = models.IntegerField(default=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.timing})"


class FeePackage(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    days = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.days} days"


class Student(models.Model):

    BELT_CHOICES = [
        ('White', 'White'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Brown', 'Brown'),
        ('Black', 'Black'),
        
    ]

    name = models.CharField(max_length=100,null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)

    address = models.TextField(
        blank=True,
        null=True,
    )

    photo = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True,
    )

    belt = models.CharField(
        max_length=20,
        choices=BELT_CHOICES,
        default='White',
        null=True, blank=True
    )

    batch = models.ForeignKey(
        Batch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        
    )

    admission_date = models.DateField(null=True, blank=True)

    fee_start_date = models.DateField()

    fee_package = models.ForeignKey(
        FeePackage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    fee_end_date = models.DateField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if self.fee_start_date and self.fee_package:
            self.fee_end_date = (
                self.fee_start_date +
                timedelta(days=self.fee_package.days)
            )

        super().save(*args, **kwargs)

    def is_fee_expiring(self):
        if not self.fee_end_date:
            return False

        today = timezone.now().date()
        days_left = (self.fee_end_date - today).days

        return 0 <= days_left <= 7

    def is_fee_expired(self):
        if not self.fee_end_date:
            return False

        today = timezone.now().date()

        return today > self.fee_end_date

    def __str__(self):
        return self.name