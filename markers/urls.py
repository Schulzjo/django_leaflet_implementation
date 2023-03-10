from django.urls import path

from markers.views import markers_map_view

app_name = "markers"

urlpatterns = [
    path("map/", markers_map_view),
]

