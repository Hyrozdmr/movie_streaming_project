from django.db import models
from django.conf import settings  # Import settings to use AUTH_USER_MODEL


class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)
    backdrop_path = models.CharField(max_length=255)
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    media_type = models.CharField(
        max_length=10,
        choices=[('movie', 'Movie')],
        default='movie'
    )

    def __str__(self):
        return self.title


class TVShow(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)
    backdrop_path = models.CharField(max_length=255)
    first_air_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    media_type = models.CharField(
        max_length=10,
        choices=[('tv', 'TV Show')],
        default='tv'
    )

    def __str__(self):
        return self.title


class WatchList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the custom User model
        on_delete=models.CASCADE,
        related_name="user_watchlist"
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, null=True, blank=True, related_name="in_watchlists"
    )
    tv_show = models.ForeignKey(
        TVShow, on_delete=models.CASCADE, null=True, blank=True, related_name="in_watchlists"
    )
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Watchlist Item"

    class Meta:
        unique_together = ('user', 'movie', 'tv_show')
