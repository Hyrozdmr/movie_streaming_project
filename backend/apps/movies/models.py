from django.db import models
from django.contrib.auth.models import User

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255)
    media_type = models.CharField(max_length=10)  # 'movie' or 'tv'
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie_id', 'media_type')