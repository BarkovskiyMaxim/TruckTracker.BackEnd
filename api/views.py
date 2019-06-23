from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .model_converters import encode_driver, encode_cargo, encode_truck, encode_shipping, encode_path
import json


from .models import Truck, Driver, Cargo, Shipping, Path

def add_headers(response):
    response['Access-Control-Allow-Origin']='*'
    response["Access-Control-Allow-Headers"] = "*"
    response["Access-Control-Allow-Credentials"] = "true"  
    return response

def driver(request, driver_id):
    d = get_object_or_404(Driver, pk=driver_id)
    return add_headers((json.dumps(encode_driver(d))))

def drivers(request):
    ds = Driver.objects.all()
    s = []
    for d in ds:
        s.append(encode_driver(d))
    return add_headers(HttpResponse(json.dumps(s)))

def truck(request, track_id):
    t = get_object_or_404(Truck, pk=driver_id)
    return add_headers(HttpResponse(json.dumps(encode_truck(t))))

def trucks(request):
    ts = Truck.objects.all()
    s = []
    for t in ts:
        s.append(encode_truck(t))
    return add_headers(HttpResponse(json.dumps(s)))

def cargo(request, cargo_id):
    c = get_object_or_404(Cargo, pk=cargo_id)
    return add_headers(HttpResponse(json.dumps(encode_cargo(c))))

def cargoes(request):
    cs = Cargo.objects.all()
    s = []
    for c in cs:
        s.append(encode_cargo(c))
    return add_headers(HttpResponse(json.dumps(encode_cargo(c))))

def shipping(request, shipping_id):
    s = get_object_or_404(Shipping, pk=shipping_id)
    return add_headers(HttpResponse(json.dumps(encode_shipping(s))))

def shippings(request):
    ss = Shipping.objects.all()
    s = []
    for sh in ss:
        s.append(encode_shipping(sh))
    return add_headers(HttpResponse(json.dumps(s)))

def shipping_add(request):
    print(request.body)
    if len(request.body) == 0:
        return add_headers(HttpResponse("false"))
    data = json.loads(request.body)
    d = Driver.objects.get(pk=data['driver_id'])
    c = Cargo.objects.get(pk=1)
    t = Truck.objects.get(pk=data['truck_id'])
    Shipping.objects.create(
        name = data['name'],
        departure = data['departure'],
        destination = data['destination'],
        predicted_duration = data['predicted_duration'],
        departure_time = data['departure_time'],
        arrival_time = data['arrival_time'],
        driver_id = d,
        cargo_id = c,
        truck_id = t 
    )
    return add_headers(HttpResponse("true"))

def current_position(request, track_id):
    p = Path.objects.filter(track_id=track_id).order_by('-num')[:1]
    if p.count() == 0:
        raise Http404
    return add_headers(HttpResponse(json.dumps(encode_path(p[0]))))

def path(request, track_id):
    ps = Path.objects.filter(track_id=track_id).order_by('num')
    s = []
    for p in ps:
        s.append(encode_path(p))
    return add_headers(HttpResponse(json.dumps(s)))

# Create your views here.
