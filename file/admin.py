from django.contrib import admin
from .models import File


@admin.register(File)
class UserAdmin(admin.ModelAdmin):
    pass
