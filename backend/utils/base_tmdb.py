class BaseTMDBClient:
    BASE_URL = "https://api.themoviedb.org/3"
    API_KEY = settings.TMDB_API_KEY

    @staticmethod
    def _fetch_data(endpoint, params):
        params['api_key'] = BaseTMDBClient.API_KEY
        try:
            response = requests.get(f"{BaseTMDBClient.BASE_URL}/{endpoint}", params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

class TMDBClient(BaseTMDBClient):
    
    @staticmethod
    def search_media(query, media_type='all', page=1):
        """
        Searches movies or TV shows or both by query.
        - media_type: 'movie', 'tv', or 'all' (default: both).
        """
        if media_type not in ['movie', 'tv', 'all']:
            return {"error": "Invalid media type. Choose 'movie', 'tv', or 'all'."}
        
        if media_type == 'all':  # Search both movie and tv
            movie_results = TMDBClient._fetch_data('search/movie', {'query': query, 'page': page})
            tv_results = TMDBClient._fetch_data('search/tv', {'query': query, 'page': page})
            return {'movies': movie_results.get('results', []), 'tv': tv_results.get('results', [])}
        elif media_type == 'movie':
            return TMDBClient._fetch_data('search/movie', {'query': query, 'page': page})
        elif media_type == 'tv':
            return TMDBClient._fetch_data('search/tv', {'query': query, 'page': page})
