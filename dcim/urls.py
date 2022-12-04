from django.urls import path

from dcim.views import IndexView,TotalDCView

urlpatterns = [
    path('index/',IndexView.as_view(),name='index'),
    path('total_dc/',TotalDCView.as_view()),
]