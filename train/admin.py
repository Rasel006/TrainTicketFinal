from django.contrib import admin
from . import models
# Register your models here.
class StationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display = ['name', 'slug']

admin.site.register(models.Train_list)
admin.site.register(models.Station, StationAdmin)