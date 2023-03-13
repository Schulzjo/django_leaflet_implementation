import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.template import Context, Template
from markers.models import Marker


def markers_map_view(request):
    markers = Marker.objects.all()
    return render(request, 'map.html', {'markers': markers})


@require_http_methods(["POST"])
def markers_create_view(request):
    marker = None
    name = request.POST.get('name')
    latitude = request.POST.get('lat')
    longitude = request.POST.get('lng')
    print(name, latitude, longitude)
    if name and latitude and longitude:
        marker = Marker.objects.create(name=name, latitude=latitude, longitude=longitude)

    return render(request, 'partials/marker_list_element.html',
                  {'marker': marker, 'longitude': longitude, 'latitude': marker.latitude,
                   longitude: marker.latitude})


@require_http_methods(["DELETE"])
def markers_delete_view(request, pk):

    marker = Marker.objects.get(pk=pk)
    marker.delete()
    return HttpResponse(status=200)
