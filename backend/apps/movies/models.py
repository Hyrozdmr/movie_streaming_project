from django.db import models
from django.conf import settings

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

    def get_full_poster_path(self):
        # Assuming you use the TMDB base URL
        base_url = 'https://image.tmdb.org/t/p/w500'
        return f"{base_url}{self.poster_path}"


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

    def get_full_poster_path(self):
        # Assuming you use the TMDB base URL
        base_url = 'https://image.tmdb.org/t/p/w500'
        return f"{base_url}{self.poster_path}"
