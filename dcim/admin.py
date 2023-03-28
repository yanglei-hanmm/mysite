from django.contrib import admin

# Register your models here.
from dcim.models import DevicesSKU, DevicesType, DevicesSPU, DCRack, DCInfo, DCRackInfo

class DCRackInfoAdmin(admin.ModelAdmin):
    # fields = ('name','dc_rack')
    list_display = ('name','dc_rack')

admin.site.register(DevicesSKU)
admin.site.register(DevicesType)
admin.site.register(DevicesSPU)
admin.site.register(DCRack)
admin.site.register(DCRackInfo,DCRackInfoAdmin)
admin.site.register(DCInfo)

