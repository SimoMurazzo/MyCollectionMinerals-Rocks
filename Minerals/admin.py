from django.contrib import admin

from Minerals.models import Mineral


class MineralAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Mineral, MineralAdmin)

