import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from markers.forms import MarkerForm
from markers.models import Marker


class MarkersView(ListView):
    template_name = 'map.html'
    model = Marker
    context_object_name = 'markers'  # used in the HTML template to loop through and list contacts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_marker_form'] = MarkerForm()
        return context


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

