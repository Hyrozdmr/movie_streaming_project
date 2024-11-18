from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Movie, TVShow, WatchList
from .serializers import MovieSerializer, TVShowSerializer, WatchListSerializer
from utils.tmdb import TMDBClient

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TVShowViewSet(viewsets.ModelViewSet):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer

class WatchListViewSet(viewsets.ModelViewSet):
    serializer_class = WatchListSerializer

    def get_queryset(self):
        return WatchList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['GET'])
def fetch_popular_media(request):
    media_type = request.query_params.get('type', 'movie')
    page = request.query_params.get('page', 1)
    data = TMDBClient.get_popular_media(media_type, page)
    serializer = MovieSerializer(data['results'], many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fetch_now_playing_media(request):
    media_type = request.query_params.get('type', 'movie')
    page = request.query_params.get('page', 1)
    data = TMDBClient.get_now_playing_media(media_type, page)
    serializer = MovieSerializer(data['results'], many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fetch_upcoming_media(request):
    media_type = request.query_params.get('type', 'movie')
    page = request.query_params.get('page', 1)
    data = TMDBClient.get_upcoming_media(media_type, page)
    serializer = MovieSerializer(data['results'], many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_media(request):
    query = request.query_params.get('query', '')
    page = request.query_params.get('page', 1)
    data = TMDBClient.search_media(query, page)
    serializer = MovieSerializer(data['results'], many=True)
    return Response(serializer.data)