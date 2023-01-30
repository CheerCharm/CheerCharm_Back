from django.contrib import admin
from .models import Charm

# Register your models here.


@admin.register(Charm)
class CharmAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'is_created']
    list_display_links = ['id', 'user', 'title', 'is_created']

    @admin.display(ordering='charm__user', description='user')
    def get_user(self, obj):
        return obj.user.username
