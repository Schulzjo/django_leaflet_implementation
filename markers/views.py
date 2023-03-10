from django.shortcuts import render


def markers_map_view(request):
    return render(request, 'map.html')

