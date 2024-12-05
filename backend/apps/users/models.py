from django.db import models
from django.contrib.auth.models import User
from apps.movies.models import Movie, TVShow

class WatchList(models.Model):
    user = models.ForeignKey(User, related_name="watchlist", on_delete=models.CASCADE)
    media_type = models.CharField(max_length=50, choices=[('movie', 'Movie'), ('tv', 'TVShow')])
    movie = models.ForeignKey(Movie, related_name="watchlists", null=True, blank=True, on_delete=models.CASCADE)
    tv_show = models.ForeignKey(TVShow, related_name="watchlists", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.media_type}"
