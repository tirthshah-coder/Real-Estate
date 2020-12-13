from django.contrib import admin
from . models import Listing

# For customizig listing when admin clicks listing how page should look like


class ListingAdmin(admin.ModelAdmin):
    # What items to display
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    # What items needs to be clickable to go through
    list_display_links = ('id', 'title')
    # Filter by realtor
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')
    list_per_page = 25   # There should be 25 list only if max then pagination


# Register your models here.
admin.site.register(Listing, ListingAdmin)
