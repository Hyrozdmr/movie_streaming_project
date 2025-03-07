from rest_framework import serializers
from .models import Movie, TVShow 
from apps.users.models import WatchList

class MovieSerializer(serializers.ModelSerializer):
    poster_url = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_poster_url(self, obj):
        """Get the full URL for the movie poster."""
        return obj.get_full_poster_path()


class TVShowSerializer(serializers.ModelSerializer):
    poster_url = serializers.SerializerMethodField()

    class Meta:
        model = TVShow
        fields = '__all__'

    def get_poster_url(self, obj):
        """Get the full URL for the TV show poster."""
        return obj.get_full_poster_path()


class WatchListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source="movie", required=False, allow_null=True
    )
    tv_show_id = serializers.PrimaryKeyRelatedField(
        queryset=TVShow.objects.all(), source="tv_show", required=False, allow_null=True
    )

    class Meta:
        model = WatchList
        fields = ['id', 'user', 'movie_id', 'tv_show_id']

    def validate(self, data):
        """Ensure that either movie or tv_show is provided, but not both."""
        if not data.get('movie') and not data.get('tv_show'):
            raise serializers.ValidationError("Either 'movie' or 'tv_show' must be provided.")
        if data.get('movie') and data.get('tv_show'):
            raise serializers.ValidationError("You can only add a movie OR a TV show to your watchlist.")

        # Ensure that the movie or tv_show is not already in the user's watchlist
        user = self.context['request'].user
        
        if data.get('movie') and WatchList.objects.filter(user=user, movie=data['movie']).exists():
            raise serializers.ValidationError("This movie is already in your watchlist.")
        
        if data.get('tv_show') and WatchList.objects.filter(user=user, tv_show=data['tv_show']).exists():
            raise serializers.ValidationError("This TV show is already in your watchlist.")
        
        return data
