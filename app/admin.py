from django.contrib import admin

from .models import Stock, Material

admin.site.register(Material)
admin.site.register(Stock)
