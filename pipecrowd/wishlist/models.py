from django.db import models

# Create your models here.
class Prospect(models.Model):
    SALES_PROFESSIONAL = 'SP'
    BUSINESS = 'BU'
    TYPE_CHOICES = [
        (BUSINESS, 'Business'),
        (SALES_PROFESSIONAL, 'Sales Professional')
    ]
    type = models.CharField(
        max_length = 2,
        choices = TYPE_CHOICES,
        default = BUSINESS,
    )
    email = models.EmailField(primary_key = True)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    creation_datetime = models.DateTimeField(auto_now_add = True)
    brief = models.CharField(max_length=1000, null=True)
    confirmed = models.BooleanField(default=False)
    token = models.CharField(max_length=20, default='temp') # ToDo: Remove default

    def __str__(self):
        return self.first_name + " " + self.last_name