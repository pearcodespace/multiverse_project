from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CSVFile)
class CSVFileAdmin(admin.ModelAdmin):
    pass

# @admin.register(Text)
# class TextAdmin(admin.ModelAdmin):
#     list_display = ('text_content', 'csv_file', 'api_result')
#     search_fields = ['text_content']

#     def save_model(self, request, obj, form, change):
#         # Make sure to call save_model on the parent class
#         super().save_model(request, obj, form, change)
        
#         # Then call your method
#         obj.call_ai_for_thai_api()

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass