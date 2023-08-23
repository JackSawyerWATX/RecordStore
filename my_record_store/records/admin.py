from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
  list_display = ("artist", "album", "released", "record_label")
  
admin.site.register(Record, RecordAdmin)