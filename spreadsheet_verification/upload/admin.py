# admin.py
from django.contrib import admin
from .models import Upload

class UploadAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded_at', 'validation_result', 'is_valid')

admin.site.register(Upload, UploadAdmin)
