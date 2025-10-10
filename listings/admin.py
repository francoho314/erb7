from django.contrib import admin
from django.forms import NumberInput
from django.db import models
from .models import Listing, Subject
from django import forms
from taggit.forms import TagWidget
from django.contrib.admin.widgets import FilteredSelectMultiple

class ListingAdminForm(forms.ModelForm):
    professionals = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=FilteredSelectMultiple(verbose_name='Professionals', is_stacked=False,
            attrs={'row' : 5}), required=False, label='Select Professionals'
            )
    class Meta:
        model = Listing
        fields = [ 'title', 'doctor', 'address', 'district', 'description',
                'services', 'service', 'room_type', 'screen', 'professionals',
                'professional', 'rooms', 'photo_main', 'photo_1', 'photo_2',
                'photo_3', 'photo_4', 'photo_5', 'photo_6', 'is_published',
                ]
        widgets = {
        'services': TagWidget(), # Use Taggit's widget for tags
        }
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    form = ListingAdminForm
    list_display = 'id', 'title', 'doctor', 'is_published', 'district', 'rooms', 'tag_list', 'display_professionals'
    list_display_links = 'id', 'title',
    list_filter = ('doctor', 'services')
    list_editable = ('is_published', 'rooms')
    search_fields = ('title', 'district', 'doctor', 'doctor__name', 'services__name', 'professionals__name')
    list_per_page = 25
    ordering=['-id']
    # prepopulated_fields = {'title': ('title',)}
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size':'10'})},
        # models.CharField: {'widget': admin.TextInput(attrs={'size':'100'})},
        # models.TextField: {'widget': admin.Textarea(attrs={'rows':20, 'cols':100})},
    }

    show_facets = admin.ShowFacets.ALWAYS

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('services', 'professionals')
    def display_professionals(self, obj):
        return ", ".join([subject.name for subject in obj.professionals.all()]) or 'None'
    display_professionals.short_description = 'Professionals'        

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Listing, ListingAdmin)
admin.site.register(Subject)
