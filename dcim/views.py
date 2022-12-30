from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from dcim.models import DCInfo, DevicesSKU


class IndexView(View):
    def get(self,request):
        dcinfos = DCInfo.objects.all()
        return render(request,'dcim/index.html',{'dcinfos':dcinfos})

class TotalDCView(View):
    def get(self,request):
        total_dc = DCInfo.objects.all().count()
        return render(request,'dcim/total_dc.html',{'total_dc':total_dc})

class DeviceView(View):
    def get(self,request):
        devices_skus = DevicesSKU.objects.all()
        return render(request,'dcim/device_sku.html',{'devices_skus':devices_skus})