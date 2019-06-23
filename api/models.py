from django.db import models

class Truck(models.Model):
    model = models.CharField(max_length=128)
    production_year = models.DateField()
    mileage = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    length = models.PositiveIntegerField()
    mass = models.PositiveIntegerField()
    load_capacity = models.PositiveIntegerField()
    axes_number = models.PositiveIntegerField()
    
class Driver(models.Model):
    MAN='m'
    FEMALE='f'
    
    GENDER_CHOICES = [
        (MAN, 'man'),
        (FEMALE, 'female')
    ]
    
    name = models.CharField(max_length = 128)
    gender = models.CharField(max_length = 1, choices=GENDER_CHOICES)
    birth_day=models.DateField()
    foto=models.ImageField(max_length = 128)
    
class Cargo(models.Model):
    name = models.CharField(max_length = 128)
    owner = models.CharField(max_length = 128)
    weight = models.PositiveIntegerField()
    cargo_type = models.CharField(max_length = 128)
    danger = models.BooleanField(default=False)
    
class Shipping(models.Model):
    name = models.CharField(max_length=128)
    departure = models.CharField(max_length=128)
    destination = models.CharField(max_length=128)
    predicted_duration = models.PositiveIntegerField()
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField(null = True)
    driver_id = models.ForeignKey(Driver, models.SET_NULL, null=True)
    truck_id = models.ForeignKey(Truck, models.SET_NULL, null=True)
    cargo_id = models.ForeignKey(Cargo, models.SET_NULL, null=True)
    route = models.TextField(null=True)

class Path(models.Model):
    track_id = models.PositiveIntegerField()
    num = models.PositiveIntegerField()
    coord = models.CharField(max_length = 128)
# Create your models here.
