from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .model_converters import encode_driver, encode_cargo, encode_truck, encode_shipping
import json


from .models import Truck, Driver, Cargo, Shipping

def driver(request, driver_id):
    d = get_object_or_404(Driver, pk=driver_id)
    return HttpResponse(json.dumps(encode_driver(d)))

def drivers(request):
    ds = Driver.objects.all()
    s = []
    for d in ds:
        s.append(encode_driver(d))
    return HttpResponse(json.dumps(s))

def driver_add(request):
    d = Driver()
    d.save()
    return HttpResponse(json.dumps(encode_driver(d)))

def truck(request, track_id):
    t = get_object_or_404(Truck, pk=driver_id)
    return HttpResponse(json.dumps(encode_truck(t)))

def trucks(request):
    ts = Truck.objects.all()
    s = []
    for t in ts:
        s.append(encode_truck(t))
    return HttpResponse(json.dumps(s))

def cargo(request, cargo_id):
    c = get_object_or_404(Cargo, pk=cargo_id)
    return HttpResponse(json.dumps(encode_cargo(c)))

def cargoes(request):
    cs = Cargo.objects.all()
    s = []
    for c in cs:
        s.append(encode_cargo(c))
    return HttpResponse(json.dumps(encode_cargo(c)))

def shipping(request, shipping_id):
    s = get_object_or_404(Shipping, pk=shipping_id)
    h = HttpResponse(json.dumps(encode_shipping(s)))
    h['Access-Control-Allow-Origin']='*'
    h["Access-Control-Allow-Headers"] = "*"
    h["Access-Control-Allow-Credentials"] = "true"    
    return h

def shippings(request):
    ss = Shipping.objects.all()
    s = []
    for sh in ss:
        s.append(encode_shipping(sh))
    h = HttpResponse(json.dumps(s))
    h['Access-Control-Allow-Origin']='*'
    h["Access-Control-Allow-Headers"] = "*"
    h["Access-Control-Allow-Credentials"] = "true"  
    return h

def test_get(request):
    if(request.method == "GET"):
        return HttpResponse(json.dumps([{ "a":"b" }, { "a":"c" }]))
    else:
        raise Http404
        
def test_post(request):
    if(request.method == "POST"):
        return HttpResponse("true")
    else:
        raise Http404

# Create your views here.
