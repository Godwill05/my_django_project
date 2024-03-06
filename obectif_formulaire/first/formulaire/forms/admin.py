from django.contrib import admin
from .models import info
# Register your models here.

admin.site.register(info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('nom')
    search_fields = ('nom')