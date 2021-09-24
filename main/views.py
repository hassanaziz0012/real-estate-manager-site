from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Listing
from pprint import pprint

# Create your views here.
def index(request):
    search_matches = request.GET.getlist('listings', None)
    if search_matches:
        listings = []
        for id in search_matches:
            listings.append(Listing.objects.get(pk=id))
    else:
        listings = None
        
    featured_listings = Listing.objects.all()[:3]
    return render(request, 'index.html', context={'listings': listings, 'featured_listings': featured_listings})

def resident_services(request):
    return render(request, 'resident_services.html')

def contact(request):
    return render(request, 'contact.html')

def listings(request):
    search_matches = request.GET.getlist('listings', None)
    if search_matches:
        listings = []
        for id in search_matches:
            listings.append(Listing.objects.get(pk=id))
    else:
        listings = Listing.objects.all()

    if request.method == 'POST':
        print(request.POST)
    return render(request, 'listings.html', context={'listings': listings})

def search_listings(request):
    if request.method == 'POST':
        address = request.POST.get('address', None)
        city = request.POST.get('city', None)
        zip_code = request.POST.get('zip_code', None)
        bath_min, bath_max = request.POST.get('bath_min', None), request.POST.get('bath_max', None)
        beds_min, beds_max = request.POST.get('beds_min', None), request.POST.get('beds_max', None)
        price_min, price_max = request.POST.get('price_min', None), request.POST.get('price_max', None)

        listings = Listing.objects.filter(
            address__icontains=address, city__contains=city, zip_code=zip_code, price__gte=price_min, price__lte=price_max, 
            baths_count__gte=bath_min, baths_count__lte=bath_max, beds_count__gte=beds_min, beds_count__lte=beds_max
            )
        matched_ids = list(listings.values_list('id', flat=True))
        matched_ids_query = ''
        for id in matched_ids:
            matched_ids_query += f'listings={id}&'
        

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(f'{next}?{matched_ids_query}')

def listing_detail(request, id):
    listing = Listing.objects.get(pk=id)
    listing_images = Paginator(listing.images.all().order_by('-id'), 3)
    
    image_groups = []
    for i in listing_images.page_range:
        image_groups.append(listing_images.page(i).object_list)

    return render(request, 'listing_detail.html', context={'listing': listing, 'image_groups': image_groups})

def admin(request):
    return render(request, 'admin.html', context={'listings': Listing.objects.all().order_by('-id')})
