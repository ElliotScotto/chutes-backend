from django.contrib import admin
from .models import UserCustom, Scrap
# Register your models here.

class UserCustomAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'address', 'city')

class ScrapAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_username', 'category')

    def owner_username(self, obj):
        return obj.owner.username

    owner_username.short_description = 'Owner Username'

admin.site.register(UserCustom, UserCustomAdmin)
admin.site.register(Scrap, ScrapAdmin)