from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)
    backdrop_path = models.CharField(max_length=255)
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    media_type = models.CharField(max_length=10, default='movie')

class TVShow(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)
    backdrop_path = models.CharField(max_length=255)
    first_air_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    media_type = models.CharField(max_length=10, default='tv')

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    media_type = models.CharField(max_length=10)
    added_date = models.DateTimeField(auto_now_add=True)