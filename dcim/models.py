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
    name = models.CharField(max_length=20,verbose_name='机柜名称')
    # power_used = models
    dc_id = models.ForeignKey('DCInfo', verbose_name='所属机房', on_delete=models.CASCADE)
    power_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='可用功率')
    power_used = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='已用功率')
    unite = models.CharField(max_length=20, verbose_name='功率单位')

    class Meta:
        db_table = 'df_rack_info'
        verbose_name = '机柜信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 机柜详情
class DCRackInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='槽位编号')
    device_name = models.ForeignKey('DevicesSKU', verbose_name='所属设备', on_delete=models.CASCADE)
    dc_rack_id = models.ForeignKey('DCRack', verbose_name='所属机柜', on_delete=models.CASCADE)
    used = models.BooleanField(verbose_name='是否空闲',)

    class Meta:
        db_table = 'df_rack_info_details'
        verbose_name = '机柜详情'
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

    def __str__(self):
        return self.name
        
class DevicesSKU(models.Model):
    '''设备SKU模型类'''

    type = models.ForeignKey('DevicesType', verbose_name='设备种类', on_delete=models.CASCADE)
    goods = models.ForeignKey('Devices', verbose_name='设备SPU', on_delete=models.CASCADE)

    name = models.CharField(max_length=20, verbose_name='设备名称')
    size = models.CharField(max_length=20, verbose_name='设备U数')
    desc = models.CharField(max_length=256, verbose_name='设备简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='设备价格')
    unit = models.CharField(max_length=20, verbose_name='设备单位')
    image_front = models.ImageField(upload_to='goods', verbose_name='设备正面图片')
    image_behind = models.ImageField(upload_to='goods', verbose_name='设备反面图片')

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