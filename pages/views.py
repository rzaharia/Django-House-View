from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
from listings.choises import price_choises, bedroom_choises, state_choises


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choises': state_choises,
        'bedroom_choises': bedroom_choises,
        'price_choises': price_choises,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all packets
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
