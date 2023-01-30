from django.contrib import admin
from .models import Cheer

# Register your models here.


@admin.register(Cheer)
class CheerAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'content', 'get_charm']
    list_display_links = ['id', 'nickname', 'content', 'get_charm']

    @admin.display(ordering='cheer__charm', description='charm')
    def get_charm(self, obj):
        return obj.charm.title
