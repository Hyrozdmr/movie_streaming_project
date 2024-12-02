import requests
import os

class TMDBClient:
    BASE_URL = "https://api.themoviedb.org/3"
    API_KEY = os.getenv("TMDB_API_KEY")  # Ensure this is set in your environment variables

    @staticmethod
    def get_popular_media(media_type='movie', page=1):
        """
        Fetches popular movies or TV shows from TMDb.
        """
        endpoint = f"{TMDBClient.BASE_URL}/{media_type}/popular"
        params = {
            'api_key': TMDBClient.API_KEY,
            'page': page,
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_now_playing_media(media_type='movie', page=1):
        """
        Fetches movies or TV shows currently playing/airing.
        """
        endpoint = f"{TMDBClient.BASE_URL}/{media_type}/now_playing"
        params = {
            'api_key': TMDBClient.API_KEY,
            'page': page,
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_upcoming_media(media_type='movie', page=1):
        """
        Fetches upcoming movies or TV shows.
        """
        endpoint = f"{TMDBClient.BASE_URL}/{media_type}/upcoming"
        params = {
            'api_key': TMDBClient.API_KEY,
            'page': page,
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def search_media(query, page=1):
        """
        Searches movies or TV shows by query.
        """
        endpoint = f"{TMDBClient.BASE_URL}/search/multi"
        params = {
            'api_key': TMDBClient.API_KEY,
            'query': query,
            'page': page,
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
