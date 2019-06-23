from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('driver/', views.drivers, name='drivers'),
    path('driver/add/', views.driver_add, name='driver_add'),
    path('driver/<driver_id>/', views.driver, name='driver'),
    path('truck/', views.trucks, name='trucks'),
    path('truck/<truck_id>/', views.truck, name = 'truck'),
    path('cargo/', views.cargoes, name='cargoes'),
    path('cargo/<cargo_id>/', views.cargo, name='cargo'),
    path('shipping/', views.shippings, name='shippings'),
    path('shipping/<shipping_id>/', views.shipping, name='shipping'),
    path('test_get/', views.test_get, name='test_get'),
    path('test_post/', views.test_post, name='test_post'),
]
