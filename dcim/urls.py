from django.urls import path

from dcim.views import IndexView,TotalDCView,DeviceView, DCRackInfoView

urlpatterns = [
    path('index/',IndexView.as_view(),name='index'),
    path('total_dc/',TotalDCView.as_view()),
    path('device/',DeviceView.as_view()),
    path('dcrackinfo/',DCRackInfoView.as_view()),
]