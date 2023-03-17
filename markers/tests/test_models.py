import pytest
from markers.models import Marker


@pytest.mark.django_db
def test_marker_create():
    marker = Marker.objects.create(name="test", latitude=13.123, longitude=2.123)
    assert marker.name == "test"
    assert marker.latitude == 13.123
    assert marker.longitude == 2.123


@pytest.mark.django_db
def test_marker_update():
    marker = Marker.objects.create(name="test", latitude=13.123, longitude=2.123)
    marker.name = "test2"
    marker.save()
    assert marker.name == "test2"


@pytest.mark.django_db
def test_marker_delete():
    marker = Marker.objects.create(name="test", latitude=13.123, longitude=2.123)
    marker.delete()
    assert Marker.objects.count() == 0
