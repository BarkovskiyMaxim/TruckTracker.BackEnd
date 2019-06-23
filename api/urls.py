from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('driver/', views.drivers, name='drivers'),
    path('driver/<driver_id>/', views.driver, name='driver'),
    path('truck/', views.trucks, name='trucks'),
    path('truck/<truck_id>/', views.truck, name = 'truck'),
    path('cargo/', views.cargoes, name='cargoes'),
    path('cargo/<cargo_id>/', views.cargo, name='cargo'),
    path('shipping/', views.shippings, name='shippings'),
    path('shipping/<shipping_id>/', views.shipping, name='shipping'),
    path('shipping_add/', views.shipping_add),
    path('current_position/<track_id>/', views.current_position),
    path('path/<track_id>/', views.path)
]
