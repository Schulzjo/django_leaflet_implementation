from django.urls import path

from markers.views import markers_create_view, markers_delete_view, MarkersView

app_name = "markers"

urlpatterns = [
    path("map/", MarkersView.as_view(), name="map"),
    path("map/create/", markers_create_view, name="create"),
    path("map/delete/<int:pk>", markers_delete_view, name="delete"),
]
