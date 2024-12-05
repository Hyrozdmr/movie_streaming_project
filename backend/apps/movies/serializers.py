from rest_framework import serializers
from .models import Movie, TVShow, WatchList

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['poster_path'] = instance.get_full_poster_path()  # Get the full URL
        return representation


class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['poster_path'] = instance.get_full_poster_path()  # Get the full URL
        return representation


class WatchListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(required=False)
    tv_show = TVShowSerializer(required=False)

    class Meta:
        model = WatchList
        fields = '__all__'

    def validate(self, data):
        # Ensure that either movie or tv_show is present
        if not data.get('movie') and not data.get('tv_show'):
            raise serializers.ValidationError("Either 'movie' or 'tv_show' must be provided.")
        return data
