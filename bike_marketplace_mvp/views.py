from django.shortcuts import render, get_object_or_404

from models import Bike

def detail(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    return render(request, 'detail.html', {'bike': bike})

def search(request):
    bikes = Bike.objects.all()
    return render(request, 'search.html', {'bikes': bikes})