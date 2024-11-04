from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'photo')
    list_filter = ('birth_date',)
    search_fields = ('user',)
    date_hierarchy = 'birth_date'
    ordering = ('birth_date',)
    raw_id_fields = ('user',)
