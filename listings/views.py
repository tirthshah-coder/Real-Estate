from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    # Fetching from database
    # listings = Listing.objects.all()  // If we want to show not any particular order

    # We want by list date as desc so -list_date i.e.last item added to database shown first
    # If is_published selected true by admin then only show
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Max 6 listing will show after that pagination
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        # This 'listings' will be reference to listings.html
        'listings': paged_listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)  # pk= Primary Key
    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    return render(request, 'listings/search.html', context)
