from django.contrib import admin

from app_restapi.models import AppPost

# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ('video_title', 'video_desc', 'video_file',\
        'video_created_at')
    list_filter = ('video_title',)
    
admin.site.register(AppPost, AdminPost)

admin.site.site_title = "SMS"
admin.site.site_header = "SMS"
admin.site.app_index = "SMS"