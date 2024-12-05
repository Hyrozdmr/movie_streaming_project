from .base_tmdb import BaseTMDBClient

class TMDBMoviesClient(BaseTMDBClient):

    @classmethod
    def get_popular(cls, page=1):
        return cls._fetch_data("movie/popular", {'page': page})

    @classmethod
    def get_now_playing(cls, page=1):
        return cls._fetch_data("movie/now_playing", {'page': page})

    @classmethod
    def get_upcoming(cls, page=1):
        return cls._fetch_data("movie/upcoming", {'page': page})

    @classmethod
    def get_top_rated(cls, page=1):
        return cls._fetch_data("movie/top_rated", {'page': page})
