from django.db import models

from core.models import TimeStamp

# Create your models here.
class Product(TimeStamp):
    name       = models.CharField(max_length=50)
    price      = models.DecimalField(max_digits=10, decimal_places=2)
    full_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_out   = models.BooleanField()
    tag        = models.CharField(max_length=30)

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    name    = models.ImageField(upload_to="") # 파일이 저장되는 중간 경로 설정할 수 있는 옵션
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'
