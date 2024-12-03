from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    # Relationships to Movie and TVShow models
    watchlist = models.ManyToManyField('movies.Movie', related_name='users_movie_watchlist')
    watchlist_tv = models.ManyToManyField('movies.TVShow', related_name='users_tv_watchlist')

    # Specify custom related_name for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom reverse relationship for groups
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Custom reverse relationship for user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user'
    )
