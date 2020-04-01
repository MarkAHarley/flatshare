
from django.contrib import admin
from flatshare.models import Flat, UserProfile, Like, Match

class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'rent')

class UserAdmin(admin.ModelAdmin):
    list_display = ('FirstName','LastName')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('l_flat','l_user')

class MatchAdmin(admin.ModelAdmin):
    list_display = ('m_flat','m_user')



admin.site.register(Flat,FlatAdmin)
admin.site.register(UserProfile,UserAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(Match,MatchAdmin)

# Register your models here.
