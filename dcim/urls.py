from django.urls import path

from dcim.views import IndexView,TotalDCView,DeviceView

urlpatterns = [
    path('index/',IndexView.as_view(),name='index'),
    path('total_dc/',TotalDCView.as_view()),
    path('device/',DeviceView.as_view()),
]