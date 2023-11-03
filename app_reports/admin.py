from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ClothDescription)
class ClothDescription(admin.ModelAdmin):
    pass