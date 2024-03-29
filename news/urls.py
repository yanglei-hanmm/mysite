from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
    path('set_cookie/',views.set_cookie),
    path('get_cookie/',views.get_cookie),
    path('index/',views.index),
    path('login/',views.login),
    path('table_image/',views.table_image),
]