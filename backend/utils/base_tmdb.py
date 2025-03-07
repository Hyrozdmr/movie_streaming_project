import logging
import requests
import os
from django.core.cache import cache
from django.conf import settings

# Set up logging
logger = logging.getLogger(__name__)

class BaseTMDBClient:
    BASE_URL = "https://api.themoviedb.org/3"
    API_KEY = os.getenv("TMDB_API_KEY") or getattr(settings, "TMDB_API_KEY", None)

    @staticmethod
    def _fetch_data(endpoint, params=None):
        """Fetch data from TMDB API with caching."""
        if params is None:
            params = {}

        if not BaseTMDBClient.API_KEY:
            logger.error("TMDB API key is missing. Check your .env file.")
            return {"error": "Missing TMDB API key"}

        # Caching to reduce API calls
        cache_key = f"tmdb_{endpoint}_{params.get('page', 1)}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data

        params["api_key"] = BaseTMDBClient.API_KEY
        url = f"{BaseTMDBClient.BASE_URL}/{endpoint}"

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            json_data = response.json()
            cache.set(cache_key, json_data, timeout=600)  # Cache for 10 minutes
            return json_data
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            return {"error": "HTTP error occurred", "details": str(http_err)}
        except requests.exceptions.ConnectionError as conn_err:
            logger.error(f"Connection error: {conn_err}")
            return {"error": "Connection error", "details": str(conn_err)}
        except requests.exceptions.Timeout as timeout_err:
            logger.error(f"Timeout error: {timeout_err}")
            return {"error": "Timeout error", "details": str(timeout_err)}
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request error occurred: {req_err}")
            return {"error": "Request error", "details": str(req_err)}


class TMDBClient(BaseTMDBClient):
    """Client for searching movies and TV shows."""

    @staticmethod
    def search_media(query, media_type="all", page=1):
        """Searches movies, TV shows, or both based on a query."""
        valid_types = ["movie", "tv", "all"]
        if media_type not in valid_types:
            return {"error": "Invalid media type. Use 'movie', 'tv', or 'all'."}

        if media_type == "movie":
            return TMDBClient._fetch_data("search/movie", {"query": query, "page": page})
        elif media_type == "tv":
            return TMDBClient._fetch_data("search/tv", {"query": query, "page": page})
        else:
            return {
                "movies": TMDBClient._fetch_data("search/movie", {"query": query, "page": page}).get("results", []),
                "tv": TMDBClient._fetch_data("search/tv", {"query": query, "page": page}).get("results", []),
            }
