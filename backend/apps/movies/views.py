from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.tmdb_movies import TMDBMoviesClient
from utils.tmdb_tvshows import TMDBTVShowsClient
from utils.base_tmdb import TMDBClient
from .models import Movie, TVShow, WatchList
from .serializers import MovieSerializer, TVShowSerializer

@api_view(['GET'])
def fetch_movies(request):
    selection = request.query_params.get('selection', 'popular')
    page = int(request.query_params.get('page', 1))
    client_methods = {
        'popular': TMDBMoviesClient.get_popular,
        'now_playing': TMDBMoviesClient.get_now_playing,
        'upcoming': TMDBMoviesClient.get_upcoming,
        'top_rated': TMDBMoviesClient.get_top_rated,
    }

    # Validate selection
    if selection not in client_methods:
        return Response({"error": "Invalid selection type for movies. Valid options are 'popular', 'now_playing', 'upcoming', 'top_rated'."}, status=400)
    
    # Fetch movie data from the TMDB client
    data = client_methods[selection](page)
    if not data.get('results'):
        return Response({"error": "No data found for this selection."}, status=404)
    
    # Serialize and return movie data
    movie_serializer = MovieSerializer(data['results'], many=True)
    return Response(movie_serializer.data)


@api_view(['GET'])
def fetch_tvshows(request):
    selection = request.query_params.get('selection', 'popular')
    page = int(request.query_params.get('page', 1))
    client_methods = {
        'popular': TMDBTVShowsClient.get_popular,
        'airing_today': TMDBTVShowsClient.get_airing_today,
        'on_tv': TMDBTVShowsClient.get_on_tv,
        'top_rated': TMDBTVShowsClient.get_top_rated,
    }

    # Validate selection
    if selection not in client_methods:
        return Response({"error": "Invalid selection type for TV shows. Valid options are 'popular', 'airing_today', 'on_tv', 'top_rated'."}, status=400)
    
    # Fetch TV show data from the TMDB client
    data = client_methods[selection](page)
    if not data.get('results'):
        return Response({"error": "No data found for this selection."}, status=404)
    
    # Serialize and return TV show data
    tv_serializer = TVShowSerializer(data['results'], many=True)
    return Response(tv_serializer.data)


@api_view(['GET'])
def search_media(request):
    query = request.query_params.get('query', '')
    media_type = request.query_params.get('type', 'all')  # Default to searching both
    page = int(request.query_params.get('page', 1))
    
    # Ensure valid media type
    if media_type not in ['movie', 'tv', 'all']:
        return Response({"error": "Invalid media type. Please use 'movie', 'tv', or 'all'."}, status=400)
    
    # Fetch search results from TMDBClient
    data = TMDBClient.search_media(query, media_type, page)
    if not data:
        return Response({"error": "No search results found."}, status=404)
    
    # Handle all media type (movie and tv)
    if media_type == 'all':
        movie_serializer = MovieSerializer(data['movies'], many=True)
        tv_serializer = TVShowSerializer(data['tv'], many=True)
        return Response({
            'movies': movie_serializer.data,
            'tv_shows': tv_serializer.data
        })
    elif media_type == 'movie':
        movie_serializer = MovieSerializer(data, many=True)
        return Response(movie_serializer.data)
    elif media_type == 'tv':
        tv_serializer = TVShowSerializer(data, many=True)
        return Response(tv_serializer.data)
