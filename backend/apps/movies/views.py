from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from utils.tmdb_movies import TMDBMoviesClient
from utils.tmdb_tvshows import TMDBTVShowsClient
from utils.base_tmdb import TMDBClient
from apps.users.models import WatchList
from .serializers import MovieSerializer, TVShowSerializer, WatchListSerializer

class FetchMoviesViewSet(viewsets.ViewSet):
    """Fetch movies from TMDB API."""

    def list(self, request):
        """Fetch movies based on query parameters (selection & page)."""
        selection = request.query_params.get('selection', 'popular')
        page = int(request.query_params.get('page', 1))

        client_methods = {
            'popular': TMDBMoviesClient.get_popular,
            'now_playing': TMDBMoviesClient.get_now_playing,
            'upcoming': TMDBMoviesClient.get_upcoming,
            'top_rated': TMDBMoviesClient.get_top_rated,
        }

        if selection not in client_methods:
            return Response(
                {"error": "Invalid selection. Choose from 'popular', 'now_playing', 'upcoming', 'top_rated'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = client_methods[selection](page)
        
        if not data or not data.get('results'):
            return Response({"error": "No movies found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "page": data.get('page'),
            "total_pages": data.get('total_pages'),
            "results": MovieSerializer(data['results'], many=True).data
        })


class FetchTVShowsViewSet(viewsets.ViewSet):
    """Fetch TV Shows from TMDB API."""

    def list(self, request):
        """Fetch TV shows based on query parameters (selection & page)."""
        selection = request.query_params.get('selection', 'popular')
        page = int(request.query_params.get('page', 1))

        client_methods = {
            'popular': TMDBTVShowsClient.get_popular,
            'airing_today': TMDBTVShowsClient.get_airing_today,
            'on_tv': TMDBTVShowsClient.get_on_tv,
            'top_rated': TMDBTVShowsClient.get_top_rated,
        }

        if selection not in client_methods:
            return Response(
                {"error": "Invalid selection. Choose from 'popular', 'airing_today', 'on_tv', 'top_rated'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = client_methods[selection](page)
        
        if not data or not data.get('results'):
            return Response({"error": "No TV shows found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "page": data.get('page'),
            "total_pages": data.get('total_pages'),
            "results": TVShowSerializer(data['results'], many=True).data
        })


class WatchListViewSet(viewsets.ModelViewSet):
    """Manage user watchlists."""
    
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return only the authenticated user's watchlist."""
        return WatchList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Ensure the watchlist entry belongs to the logged-in user."""
        serializer.save(user=self.request.user)


class SearchMediaViewSet(viewsets.ViewSet):
    """Search for movies or TV shows."""

    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search for movies or TV shows based on query."""
        query = request.query_params.get('query', '')
        media_type = request.query_params.get('type', 'all')
        page = int(request.query_params.get('page', 1))

        if media_type not in ['movie', 'tv', 'all']:
            return Response({"error": "Invalid media type. Use 'movie', 'tv', or 'all'."}, status=status.HTTP_400_BAD_REQUEST)

        data = TMDBClient.search_media(query, media_type, page)

        if not data:
            return Response({"error": "No search results found."}, status=status.HTTP_404_NOT_FOUND)

        if media_type == 'all':
            return Response({
                'movies': MovieSerializer(data.get('movies', []), many=True).data,
                'tv_shows': TVShowSerializer(data.get('tv', []), many=True).data
            })
        elif media_type == 'movie':
            return Response(MovieSerializer(data.get('results', []), many=True).data)
        elif media_type == 'tv':
            return Response(TVShowSerializer(data.get('results', []), many=True).data)
