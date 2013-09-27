from django.shortcuts import render, get_object_or_404

from models import Bike

def detail(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    picture_ids = range(1,3)

    picture_ids = {
        1: [1],
        2: [1],
        3: range(1,9),
        4: range(1,7),
        5: range(1,10),
        6: range(1,9),
        7: range(1,9),
        8: range(1,9),
    }

    return render(request, 'detail.html', {'bike': bike, 'picture_ids': picture_ids[bike.id]})

def search(request):
    bikes = Bike.objects.all()
    return render(request, 'search.html', {'bikes': bikes})