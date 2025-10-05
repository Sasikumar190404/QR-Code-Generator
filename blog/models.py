from django.db import models

# Create your models here.
class QRCodeForm(models.Model):
    restaurant_name=models.CharField(max_length=50)
    url=models.URLField(max_length=200,)
   