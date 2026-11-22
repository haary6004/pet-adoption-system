from django.contrib import admin
from .models import AdoptionRequest, Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal_type', 'age', 'is_available')
    list_filter = ('animal_type', 'is_available')
    search_fields = ('name', 'animal_type')


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('pet', 'applicant', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)


# Register your models here.
