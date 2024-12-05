from django.contrib import admin
from .models import Movie, TVShow, WatchList

# Register the Movie model with some custom display options
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'vote_average', 'vote_count', 'get_watchlist_count')
    search_fields = ('title',)
    list_filter = ('release_date', 'vote_average')
    
    def get_watchlist_count(self, obj):
        return WatchList.objects.filter(movie=obj).count()
    get_watchlist_count.short_description = 'Watchlist Count'

# Register the TVShow model with some custom display options
class TVShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_air_date', 'vote_average', 'vote_count')
    search_fields = ('title',)
    list_filter = ('first_air_date', 'vote_average')

# Register the models
admin.site.register(Movie, MovieAdmin)
admin.site.register(TVShow, TVShowAdmin)
admin.site.register(WatchList)
