from django.urls import path
from . import views

api="api/v1.0/market/company"
urlpatterns=[
    path(api+'/getall', views.getData),
    path(api+'/info/<companycode>', views.infoData),
    path(api+'/register', views.regData),
    path(api+'/delete/<companycode>', views.delData),
    path(api+'/stock/add/<companycode>', views.addData),
    path(api+'/stock/get/companycode/startdate/endate', views.delData)
]