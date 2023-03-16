import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from markers.forms import MarkerForm
from markers.models import Marker


def markers_map_view(request):
    markers = Marker.objects.all()
    add_marker_form = MarkerForm()
    return render(request, 'map.html', {'markers': markers, "add_marker_form": add_marker_form})


@require_http_methods(["POST"])
def markers_create_view(request):

    form = MarkerForm(request.POST)

    if form.is_valid():
        marker = form.save()
        return render(request, 'partials/marker_list_element.html',
                      {'marker': marker, 'longitude': marker.longitude, 'latitude': marker.latitude})


@require_http_methods(["DELETE"])
def markers_delete_view(request, pk):

    marker = Marker.objects.get(pk=pk)
    marker.delete()
    res = HttpResponse(status=200)
    res.headers["HX-Trigger"] = json.dumps({"delete_marker_from_map": pk})
    return res
