from rest_framework import serializers
from .models import Movie, TVShow, WatchList

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'