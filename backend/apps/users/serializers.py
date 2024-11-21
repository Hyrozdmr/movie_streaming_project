from rest_framework import serializers
from .models import User
from movies.serializers import MovieSerializer, TVShowSerializer

class UserSerializer(serializers.ModelSerializer):
    watchlist = MovieSerializer(many=True, read_only=True)
    watchlist_tv = TVShowSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'watchlist', 'watchlist_tv']

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['watchlist', 'watchlist_tv']