from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'nickname']
    list_display_links = ['id', 'username', 'nickname']
