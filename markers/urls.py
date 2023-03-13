from django.urls import path

from markers.views import markers_map_view, markers_create_view, markers_delete_view

app_name = "markers"

urlpatterns = [
    path("map/", markers_map_view),
    path("map/create/", markers_create_view, name="create"),
    path("map/delete/<int:pk>", markers_delete_view, name="delete"),
]
