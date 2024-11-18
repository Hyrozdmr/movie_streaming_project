from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import requests
from django.conf import settings

TMDB_API_KEY = settings.TMDB_API_KEY
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

class WatchListViewSet(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def get_queryset(self):
        return WatchList.objects.filter(user=self.request.user)

@api_view(['GET'])
def fetch_movies(request, category):
    endpoint = {
        'popular': '/movie/popular',
        'now_playing': '/movie/now_playing',
        'upcoming': '/movie/upcoming',
    }.get(category)
    
    response = requests.get(
        f"{TMDB_BASE_URL}{endpoint}",
        params={'api_key': TMDB_API_KEY}
    )
    return Response(response.json())

@api_view(['GET'])
def search_media(request):
    query = request.GET.get('query', '')
    response = requests.get(
        f"{TMDB_BASE_URL}/search/multi",
        params={
            'api_key': TMDB_API_KEY,
            'query': query
        }
    )
    return Response(response.json())