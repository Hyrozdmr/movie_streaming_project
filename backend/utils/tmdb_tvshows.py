from .base_tmdb import BaseTMDBClient

class TMDBTVShowsClient(BaseTMDBClient):

    @classmethod
    def get_popular(cls, page=1):
        return cls._fetch_data("tv/popular", {'page': page})

    @classmethod
    def get_airing_today(cls, page=1):
        return cls._fetch_data("tv/airing_today", {'page': page})

    @classmethod
    def get_on_tv(cls, page=1):
        return cls._fetch_data("tv/on_the_air", {'page': page})

    @classmethod
    def get_top_rated(cls, page=1):
        return cls._fetch_data("tv/top_rated", {'page': page})
