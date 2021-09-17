from django.db import models

# Create your models here.
class Listing(models.Model):
    address = models.CharField(max_length=300, null=False, blank=False)
    zip_code = models.IntegerField(null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    beds_count = models.IntegerField(default=1)
    baths_count = models.IntegerField(default=1)
    images = models.ManyToManyField('ListingImage', related_name='images', blank=True)

    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def get_banner(self):
        return self.images.first().file.url

    def __str__(self) -> str:
        return f'{self.address} - ${self.price}'

    def __repr__(self) -> str:
        return f'<Listing: {self.address} - ${self.price}>'


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing')
    file = models.ImageField(upload_to='listing-images', null=False, blank=False)
    
    def __str__(self) -> str:
        return f'{self.file.name} - {self.listing.address}'

    def __repr__(self) -> str:
        return f'<ListingImage: {self.file.name} - {self.listing.address}>'
