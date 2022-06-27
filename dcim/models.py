from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class DCInfo(models.Model):
    '''设备类型模型类'''
    name = models.CharField(max_length=20, verbose_name='DC名称')
    location = models.CharField(max_length=100,verbose_name='位置')

    class Meta:
        db_table = 'df_dc_info'
        verbose_name = 'DC信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class DCRack(models.Model):
    no = models.CharField(max_length=20,verbose_name='机柜编号')
    # power_used = models
    power_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='可用功率')
    power_used = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='已用功率')
    unite = models.CharField(max_length=20, verbose_name='功率单位')

    class Meta:
        db_table = 'df_rack_info'
        verbose_name = '机柜信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Devices(models.Model):
    '''设备SPU模型类'''
    name = models.CharField(max_length=20, verbose_name='设备SPU名称')
    # 富文本类型:带有格式的文本
    detail = HTMLField(blank=True, verbose_name='设备详情')

    class Meta:
        db_table = 'df_devices'
        verbose_name = '设备SPU'
        verbose_name_plural = verbose_name
        
class DevicesSKU(models.Model):
    '''设备SKU模型类'''

    type = models.ForeignKey('DevicesType', verbose_name='设备种类',on_delete=models.CASCADE)
    goods = models.ForeignKey('Devices', verbose_name='设备SPU',on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='设备名称')
    desc = models.CharField(max_length=256, verbose_name='设备简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='设备价格')
    unite = models.CharField(max_length=20, verbose_name='设备单位')
    image = models.ImageField(upload_to='goods', verbose_name='设备图片')

    class Meta:
        db_table = 'df_devices_sku'
        verbose_name = '设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    
class DevicesType(models.Model):
    '''设备类型模型类'''
    name = models.CharField(max_length=20, verbose_name='种类名称')
    logo = models.CharField(max_length=20, verbose_name='标识')
    image = models.ImageField(upload_to='type', verbose_name='设备类型图片')

    class Meta:
        db_table = 'df_devices_type'
        verbose_name = '设备种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name