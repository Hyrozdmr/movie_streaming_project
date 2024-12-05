# admin.py
from django.contrib import admin
from .models import User, WatchList
from apps.movies.models import Movie, TVShow

# Register the User model in admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')

admin.site.register(User, UserAdmin)

# Register the Watchlist model in admin
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'tv_show')
    search_fields = ('user__username', 'movie__title', 'tv_show__title')
    list_filter = ('user',)

admin.site.register(WatchList, WatchlistAdmin)