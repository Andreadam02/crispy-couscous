from django.contrib import admin
from .models import Fighter, UploadedFile
# Register your models here.

admin.site.register(Fighter)
admin.site.register(UploadedFile)