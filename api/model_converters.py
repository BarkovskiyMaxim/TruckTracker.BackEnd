from .models import Truck, Driver, Cargo, Shipping

def encode_driver(d):
    s = { 
        "id" : d.id,
        "name" : d.name,
        "gender" : d.gender,
        "birth_day" : d.birth_day.__str__()
    }
    return s

def encode_truck(t):
    s = {
        "id" : t.id,
        "model" : t.model,
        "production_year" : t.production_year.__str__(),
        "mileage" : t.mileage,
        "height" : t.height,
        "width" : t.width,
        "length" : t.length,
        "mass" : t.mass,
        "load_capacity" : t.load_capacity,
        "axes_number" : t.axes_number
    }
    return s

def encode_cargo(c):
    s = {
        "id" : c.id,
        "name" : c.name,
        "owner" : c.owner,
        "weight" : c.weight,
        "cargo_type" : c.cargo_type,
        "danger" : c.danger
    }
    return s

def encode_shipping(sh):
    s = {
        "id" : sh.id,
        "name" : sh.name,
        "departure" : sh.departure,
        "destination" : sh.destination,
        "predicted_duration" : sh.predicted_duration,
        "departure_time" : sh.departure_time.__str__(),
        "arrival_time" : sh.arrival_time.__str__(),
        "driver_id" : sh.driver_id.id,
        "driver_name" : sh.driver_id.name,
        "truck_id" : sh.truck_id.id,
        "truck_model" : sh.truck_id.model,
        "cargo_id" : sh.cargo_id.id,
        "cargo_name" : sh.cargo_id.name
    }
    return s

def encode_path(p):
    print(p.id)
    print(p.track_id)
    print(p.num)
    print(p.coord)
    s = {
        "id" : p.id,
        "track_id" : p.track_id,
        "num" : p.num,
        "coord" : p.coord
    }        
    return s
