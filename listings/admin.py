from django.contrib import admin
from django.forms import NumberInput
from django.db import models
from .models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'doctor', 'is_published', 'rooms', 'district'
    list_display_links = 'id', 'title',
    list_filter = 'doctor',
    list_editable = 'is_published', 'rooms'
    search_fields = 'title', 'district', 'doctor'
    list_per_page = 25
    ordering=['-id']
    #prepopulated_fields = {'title': ('title',)}
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size':'10'})},
        #models.CharField: {'widget': admin.TextInput(attrs={'size':'100'})},
        #models.TextField: {'widget': admin.Textarea(attrs={'rows':20, 'cols':100})},
    }

    show_facets = admin.ShowFacets.ALWAYS

admin.site.register(Listing, ListingAdmin)
