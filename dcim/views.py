from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from dcim.models import DCInfo, DevicesSKU, DCRackInfo


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

class DCRackInfoView(View):
    def get(self,request):
        # 查询信息楼机房A01机柜的槽位信息
        #DCRackInfo.objects.filter(dc_rack__name='A01', dc_rack__dc__name='信息楼机房')

        # 反向查询01槽位的机柜信息
        # DCRack.objects.filter(dcrackinfo__name='01')
        dc_rack_infos =  DCRackInfo.objects.filter(dc_rack__name='A01', dc_rack__dc__name='信息楼机房')
        # 查询信息楼机房A01机柜的设备信息
        devices_skus = DevicesSKU.objects.filter(dcrackinfo__dc_rack__name='A01',dcrackinfo__dc_rack__dc__name='信息楼机房').distinct()

        '''
        dict={
            'dc_rack_info01':{'info':<DCRackInfo: 01>,'slot':[1,2,3,4]},
            'dc_rack_info02':{'info':<DCRackInfo: 02>,'slot':[7,8]},
        }
        for d in dict:
            img = d[info][img]
            for s in slot:
                s
                
        [{'info': <DevicesSKU: sap-prod-ora01>, 'slot': [1, 2]}, {'info': <DevicesSKU: sap-prod-ora02>, 'slot': [4, 5]}]
        '''

        # dict = {}
        # for i in range(0,len(devices_skus)):
        #     slot_begin = devices_skus[i].slot_begin
        #     size = devices_skus[i].size
        #     print(slot_begin,size)
        #     j = range(slot_begin,slot_begin+size)
        #     print(j)
        #     device = {}
        #     device['info'] = devices_skus[i]
        #     device['slot'] = list(j)
        #     dict['devices_skus'+str(i)] = device
        #
        # print(dict)

        devices = []

        for i in range(0, len(devices_skus)):
            device = {}
            slot_begin = devices_skus[i].slot_begin
            size = devices_skus[i].size
            print(slot_begin, size)
            j = range(slot_begin, slot_begin + size)
            device['info'] = devices_skus[i]
            device['slot'] = list(j)
            devices.append(device)
        print(devices)

        return render(request,'dcim/dc_rack_info.html',{'devices':devices,'dc_rack_infos':dc_rack_infos,'devices_skus':devices_skus})