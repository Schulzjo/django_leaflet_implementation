import pytest

from markers.models import Marker
from django.urls import reverse


@pytest.mark.django_db
def test_markers_view(client):
    response = client.get(reverse('markers:map'))
    assert response.status_code == 200
    assert b".leaflet-container" in response.content
    print(response.content)


@pytest.mark.django_db
def test_markers_create_view(client):
    response = client.post(reverse('markers:create'), {"name": "test", "latitude": 13.123, "longitude": 2.123})
    assert response.status_code == 200
    assert b"test" in response.content
    assert b"13.123" in response.content
    assert b"2.123" in response.content


@pytest.mark.django_db
def test_markers_delete_view(client):
    marker = Marker.objects.create(name="test", latitude=13.123, longitude=2.123)
    response = client.delete(reverse('markers:delete', args=[marker.pk]))
    assert response.status_code == 200
    assert b"test" not in response.content
    assert b"13.123" not in response.content
    assert b"2.123" not in response.content
