from django.contrib import admin
from .models import Movie, TVShow
from apps.users.models import WatchList

class MovieAdmin(admin.ModelAdmin):
    """Admin configuration for the Movie model."""
    list_display = ('title', 'release_date', 'vote_average', 'vote_count', 'get_watchlist_count')
    search_fields = ('title',)
    list_filter = ('release_date', 'vote_average')
    
    def get_watchlist_count(self, obj):
        """Returns the count of users who added this movie to their watchlist."""
        return obj.watchlists.count()  # Uses the related_name on the Movie model's ForeignKey
    get_watchlist_count.short_description = 'Watchlist Count'


class TVShowAdmin(admin.ModelAdmin):
    """Admin configuration for the TVShow model."""
    list_display = ('title', 'first_air_date', 'vote_average', 'vote_count', 'get_watchlist_count')
    search_fields = ('title',)
    list_filter = ('first_air_date', 'vote_average')

    def get_watchlist_count(self, obj):
        """Returns the count of users who added this TV show to their watchlist."""
        return obj.watchlists.count()  # Uses the related_name on the TVShow model's ForeignKey
    get_watchlist_count.short_description = 'Watchlist Count'


class WatchListAdmin(admin.ModelAdmin):
    """Admin configuration for the WatchList model."""
    list_display = ('user', 'movie', 'tv_show', 'added_date')
    search_fields = ('user__username', 'movie__title', 'tv_show__title')
    list_filter = ('media_type', 'user')
    date_hierarchy = 'added_date'  # Allows filtering by date in the admin UI
    
    # This can be useful for making the admin more clear
    def get_movie_title(self, obj):
        """Returns the title of the movie in the watchlist."""
        return obj.movie.title if obj.movie else None
    
    def get_tv_show_title(self, obj):
        """Returns the title of the TV show in the watchlist."""
        return obj.tv_show.title if obj.tv_show else None
    
    get_movie_title.short_description = 'Movie Title'
    get_tv_show_title.short_description = 'TV Show Title'

    # Update `list_display` to include these new fields
    list_display = ('user', 'get_movie_title', 'get_tv_show_title', 'added_date')

# Register the models
admin.site.register(Movie, MovieAdmin)
admin.site.register(TVShow, TVShowAdmin)