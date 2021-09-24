from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administration', views.admin, name='kaj-admin'),
    path('contact', views.contact, name='contact'),
    path('resident-services', views.resident_services, name='resident-services'),
    path('listings', views.listings, name='listings'),
    path('listings/<int:id>', views.listing_detail, name='listing-detail'),
    path('search-listings', views.search_listings, name='search-listings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

