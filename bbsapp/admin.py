from django.contrib import admin

# Register your models here.
from  . import models

class bbs_admin(admin.ModelAdmin):
    list_display = ('title','summary','author','show_signature','updated_at')
    list_filter = ('title','updated_at')
    search_fields = ('title','author__user__username')

    # class Media:
    #     js = [
    #          '/media/editor/tiny_mce/tiny_mce_src.js',
    #          '/media/editor/tiny_mce/tiny_mce_config.js',
    #     ]

    def show_signature(self,obj):
        return obj.author.user.username

    show_signature.short_description = "就是你"


admin.site.register(models.Posts,bbs_admin)
admin.site.register(models.Categories)
admin.site.register(models.My_bbs_users)