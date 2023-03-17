import pytest
from markers.forms import MarkerForm


@pytest.mark.django_db
def test_marker_form_validation():
    form = MarkerForm(data={'name': 'test', 'latitude': 13.123, 'longitude': 2.123})
    assert form.is_valid()


@pytest.mark.django_db
def test_marker_form_validation_invalid():
    form = MarkerForm(data={'name': 'test', 'latitude': 'invalid', 'longitude': 2.123})
    assert not form.is_valid()


@pytest.mark.django_db
def test_marker_form_validation_missing():
    form = MarkerForm(data={'name': 'test', 'latitude': 13.123})
    assert not form.is_valid()

