from rest_framework import serializers
from .models import User
from apps.movies.models import Movie, TVShow
from .models import WatchList

class UserSerializer(serializers.ModelSerializer):
    # You can add fields you want to expose here
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'watchlist', 'watchlist_tv')  # Add relevant fields

class WatchlistSerializer(serializers.ModelSerializer):
    # You can choose to include movie and tv show details in the watchlist serializer
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), required=False)
    tv_show = serializers.PrimaryKeyRelatedField(queryset=TVShow.objects.all(), required=False)

    class Meta:
        model = WatchList
        fields = ('id', 'movie', 'tv_show', 'user')  # Make sure 'user' is included for binding

    def validate(self, attrs):
        # Custom validation to ensure that either movie or tv_show is provided, but not both
        if not attrs.get('movie') and not attrs.get('tv_show'):
            raise serializers.ValidationError("Either movie or tv_show must be provided.")
        return attrs