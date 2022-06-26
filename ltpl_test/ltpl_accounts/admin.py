from django.contrib import admin
from ltpl_accounts.models import User,UserProfile
from django.utils.html import format_html
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img height="100" width="100" src="{}" />'.format(obj.image.url if obj.image else ""))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    list_display = ["name","email","mobile","image_tag"]
    list_filter = ("mobile", )
    search_fields = ("name__icontains","email__icontains" )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user","role","location"]
    list_filter = ("date_of_birth", )
    search_fields = ("user__email__icontains","location__icontains" )