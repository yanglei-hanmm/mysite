from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from dcim.models import DCInfo


class IndexView(View):
    def get(self,request):
        dcinfos = DCInfo.objects.all()
        return render(request,'index.html',{'dcinfos':dcinfos})

class TotalDCView(View):
    def get(self,request):
        total_dc = DCInfo.objects.all().count()
        return render(request,'total_dc.html',{'total_dc':total_dc})