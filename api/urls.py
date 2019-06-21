from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('test_get/', views.test_get, name='test_get'),
    path('test_post/', views.test_post, name='test_post'),
]
