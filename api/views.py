from django.shortcuts import render
from django.http import Http404, HttpResponse

def test_get(request):
    if(request.method == "GET"):
        return HttpResponse("true")
    else:
        raise Http404
        
def test_post(request):
    if(request.method == "POST"):
        return HttpResponse("true")
    else:
        raise Http404

# Create your views here.
