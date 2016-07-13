from django.contrib import admin
from .models import WigFile



class WigFilesAdmin(admin.ModelAdmin):

	list_display = ('species', 'database', 'frame', 'specific_tissue', 'chr_name')



admin.site.register(WigFile, WigFilesAdmin)
