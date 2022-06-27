from django.contrib import admin

# Register your models here.
from dcim.models import DevicesSKU,DevicesType,Devices,DCRack,DCInfo

admin.site.register(DevicesSKU)
admin.site.register(DevicesType)
admin.site.register(Devices)
admin.site.register(DCRack)
admin.site.register(DCInfo)