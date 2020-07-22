from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from news.models import News, Profile

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
	list_display = ('text', 'created_on', 'total_likes')
	list_filter = ['created_on']
	search_fields = ['text']

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

admin.site.register(News, NewsAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)